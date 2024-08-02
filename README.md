# HTTP Request and Response Testing (Assignments)

This Python script provides a set of functions to test various HTTP requests and responses using the `httpbin.org` service.


## Features
- Test GET, POST, PUT, PATCH, and DELETE requests
- Test redirects

   
## Functions
The script includes the following functions:

1. `test_1()`: Sends a GET request to the base URL of `httpbin.org`.
2. `test_2()`: Sends a GET request to `httpbin.org/get` with a query parameter.
3. `test_3()`: Sends a POST request to `httpbin.org/post` with JSON data.
4. `test_4()`: Sends a PUT request to `httpbin.org/put` with JSON data.
5. `test_5()`: Sends a PATCH request to `httpbin.org/patch` with JSON data.
6. `test_6()`: Sends a DELETE request to `httpbin.org/delete`.
7. `test_7()`: Sends a GET request to `httpbin.org/redirect/3` and follows the redirects.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
