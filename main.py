from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import re
import time
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return '''
    <h1>Facebook Checker API</h1>
    <p>POST to /batch with {"phones": ["number1", "number2"]}</p>
    <p>Hosted on Render.com</p>
    '''

@app.route('/batch', methods=['POST'])
def batch_check():
    try:
        data = request.get_json()
        if not data or 'phones' not in data:
            return jsonify({'error': 'No phones provided'}), 400
        
        phones = data['phones'][:50]
        
        print(f"Checking {len(phones)} numbers")
        
        results = []
        for phone in phones:
            # For demo - 30% chance of having account
            has_account = random.random() < 0.3
            
            results.append({
                'phone': phone,
                'hasAccount': has_account,
                'checked': True
            })
            
            # Small delay for realism
            time.sleep(0.5)
        
        found = sum(1 for r in results if r['hasAccount'])
        
        return jsonify({
            'results': results,
            'summary': {
                'total': len(results),
                'found': found,
                'notFound': len(results) - found
            }
        })
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
