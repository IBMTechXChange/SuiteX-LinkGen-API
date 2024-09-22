# SuiteX-LinkGen-API

## Overview

**SuiteX-LinkGen-API** is a powerful API designed to simplify link generation for various services within the SuiteX ecosystem, including connectX, docX, calX, and mailX. This API enhances productivity in modern office environments by streamlining workflows and facilitating seamless integration across platforms.

## Features

- **Dynamic Link Generation**: Effortlessly create unique links for different services, ensuring quick access to essential resources.
- **Secure Passphrase Handling**: Automatically generate and encode secure passphrases to enhance link security.
- **Cross-Origin Resource Sharing (CORS)**: Supports CORS to allow requests from different origins, enabling smooth integration with front-end applications.
- **Environment Configuration**: Utilize a `.env` file for easy customization of URLs and settings without altering the source code.

## Use Cases

SuiteX-LinkGen-API is ideal for organizations looking to optimize workflows by providing quick access to vital tools and documents. Key use cases include:

- Generating links for collaborative documents (docX).
- Creating calendar event links (calX).
- Facilitating communication through email links (mailX).
- Enabling real-time collaboration in connectX.

## Getting Started

### Prerequisites

- Python 3.6+ (download from [python.org](https://www.python.org/downloads/))

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/IBMTechXChange/SuiteX-LinkGen-API.git
   cd SuiteX-LinkGen-API
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**: In the root directory, create a file named `.env` and add your service URLs:
   ```plaintext
   CONNECTX_URL=https://your-connectx-url.com
   DOCX_URL=https://your-docx-url.com
   CALX_URL=http://your-calx-url.com
   MAILX_URL=http://your-mailx-url.com
   ```

### Running the Application

Start the Flask application:
```bash
python app.py
```

The API will be accessible at `http://localhost:5000`.

## API Endpoints

### Generate Link

- **Endpoint**: `/generate_link`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "connectX": 1,
    "docX": 0,
    "calX": 0,
    "mailX": 0
  }
  ```
- **Response**:
  ```json
  {
    "connectX_link": "https://your-connectx-url.com/rooms/abcd-efgh#encoded_passphrase"
  }
  ```

### Get Link Data

- **Endpoint**: `/link/<link_id>`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "connectX": 1
  }
  ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add your feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Create a pull request.


## Contact

For questions or feedback, feel free to reach out:

- **GitHub**: [IBMTechXChange](https://github.com/IBMTechXChange)


Elevate your office's efficiency with SuiteX