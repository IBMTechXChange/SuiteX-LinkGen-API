from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import urllib.parse
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

links_storage = {}

@app.route('/', methods=['GET'])
def status_check():
    return jsonify({'status': 'works baby!'}), 200
    
@app.route('/generate_link', methods=['POST'])
def generate_link():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input provided'}), 400

    response = {}

    connectx_url = os.getenv('CONNECTX_URL')
    docx_url = os.getenv('DOCX_URL')
    calx_url = os.getenv('CALX_URL')
    mailx_url = os.getenv('MAILX_URL')

    if 'connectX' in data and data['connectX'] == 1:
        room_id = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(4)) + '-' + \
              ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(4))
        passphrase = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(64))
        encoded_passphrase = urllib.parse.quote(passphrase)
        link_id = f"{connectx_url}/rooms/{room_id}#{encoded_passphrase}"
        links_storage[link_id] = {'connectX': data['connectX']}
        response['connectX_link'] = link_id

    if 'docX' in data and data['docX'] == 1:
        link_id = str(uuid.uuid4())
        links_storage[link_id] = {'docX': data['docX']}
        response['docX_link'] = f'{docx_url}/{link_id}'  

    if 'calX' in data and data['calX'] == 1:
        link_id = str(uuid.uuid4())
        links_storage[link_id] = {'calX': data['calX']}
        response['calX_link'] = f'{calx_url}/link/{link_id}'

    if 'mailX' in data and data['mailX'] == 1:
        link_id = str(uuid.uuid4())
        links_storage[link_id] = {'mailX': data['mailX']}
        response['mailX_link'] = f'{mailx_url}/link/{link_id}'

    if not response:
        response['message'] = 'No links generated, all inputs are 0'

    return jsonify(response), 200

@app.route('/link/<link_id>', methods=['GET'])
def get_link_data(link_id):
    if link_id in links_storage:
        return jsonify(links_storage[link_id]), 200
    else:
        return jsonify({'error': 'Link not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
