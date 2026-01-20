from flask import Flask, request, jsonify
from flask_cors import CORS
import random

# Create Flask app
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Facebook Checker API is running!"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/batch', methods=['POST'])
def batch_check():
    try:
        data = request.get_json()
        phones = data.get('phones', [''])[:20]
        
        results = []
        for phone in phones:
            # Demo logic - 30% chance
            has_account = random.random() < 0.3
            
            results.append({
                'phone': phone,
                'hasAccount': has_account,
                'status': 'checked'
            })
        
        return jsonify({
            'results': results,
            'total': len(results)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# IMPORTANT: This must be at the end
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
