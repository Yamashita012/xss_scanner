# xss_scanner
A simple a simple xss scanner.

**XSS_SCANNER that uses a bunch of xss payloads:**

# Download Payload Here
### https://github.com/payloadbox/xss-payload-list


# Cross-Site Scripting (XSS) Scanner

This Python script is designed to scan a target URL for potential Cross-Site Scripting (XSS) vulnerabilities using a list of payloads provided in a separate file. It sends HTTP GET requests with each payload appended to the target URL and checks if the payload is reflected in the response. If a payload is found in the response, it indicates a potential XSS vulnerability.

## Prerequisites

- Python 3.x
- The `requests` library, which can be installed using `pip` if not already present:

```shell
pip install requests
```

## Usage

You can use this script to test a target URL for XSS vulnerabilities. Follow these steps:

1. Open a terminal window.

2. Run the script with the following command, providing the target URL and the path to the payload file as arguments:

   ```shell
   python xss_scanner.py <target_url> <payload_file>
   ```

   - `<target_url>`: The URL of the web page you want to test for XSS vulnerabilities.
   - `<payload_file>`: The path to a text file containing a list of XSS payloads, with one payload per line.

3. The script will iterate through each payload in the specified file and send a request to the target URL with the payload appended. If it detects that the payload is reflected in the response, it will print "XSS Found" and display the successful payload. If no payload is reflected in the response, it will print "Secure" for that payload.

4. After scanning all payloads, the script will complete its execution.

## Example

Here's an example of how to use the script:

```shell
python xss_scanner.py https://example.com /path/to/payloads.txt
```

## Important Notes

- This script is for educational and testing purposes only. Do not use it to scan or exploit websites without proper authorization.

- Ensure that you have permission from the website owner before scanning their site for vulnerabilities.

- The effectiveness of the script depends on the quality and variety of payloads in the payload file.

- Keep in mind that this script is a basic tool for identifying potential XSS vulnerabilities. It may produce false positives or miss certain types of vulnerabilities.

## Disclaimer

Use this script responsibly and only on websites you have permission to test. Unauthorized testing can be illegal and unethical. The author is not responsible for any misuse or illegal activities conducted using this script.
