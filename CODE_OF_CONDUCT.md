

---

# Code of Conduct and Contribution Guidelines

This document outlines the requirements and best practices for contributing to this project. Following these guidelines helps ensure high code quality, security, and consistency throughout the repository.

## 1. General Requirements

- **Python Version**:  
  All code must be compatible with Python 3.8 and above.

- **Type Annotations**:  
  Use type annotations consistently to improve readability and maintainability.

- **Code Formatting**:  
  Before submitting a pull request, run [Black](https://black.readthedocs.io/en/stable/) to ensure your code is properly formatted.

## 2. Endpoint Implementation

- **Adding a New Endpoint**:
  - **Step 1**: Implement the endpoint in the `bpx.base` modules.
  - **Step 2**: Add the same endpoint in the `bpx` modules.
  - **Step 3**: Also include it in the `bpx.async_` modules.
  - **Documentation**:  
    Each endpoint must include a docstring with a link to the official documentation.

- **Fixing an Existing Endpoint**:
  - Apply the same process as when adding a new endpoint: first modify it in `bpx.base`, then update it in both `bpx` and `bpx.async_`.
  - Ensure that the endpoint's docstring includes the official documentation link.

## 3. Dependency Management

- **Main Dependencies**:  
  List all primary dependencies in the `requirements.txt` file.

- **Development Dependencies**:  
  List development-specific dependencies in the `requirements-dev.txt` file.

- **Adding New Dependencies**:
  1. **First**, add the dependency using [Poetry](https://python-poetry.org/).
  2. **Then**, update the corresponding `requirements.txt` or `requirements-dev.txt` file.
  3. **Important**: Do not change the version specified in the Poetry configuration.

## 4. Security and Code Integrity

- **No Malicious Code**:  
  Do not inject any malicious code into the project.

- **User-Initiated Actions**:  
  Ensure that any request or operation performed by the code is explicitly initiated by the user, and avoid unexpected or automatic actions.

## 5. Project Structure and Examples

- **Adhere to the Project Structure**:  
  Follow the established project structure when adding new features or modifying existing code.

- **Examples Directory**:
  - Do **not** add examples that alter a user’s account balance or change account settings.

## 6. Pull Request Process

- **Before Submitting**:
  - Verify that your code is formatted with Black.
  - Ensure that you have followed all the guidelines above.
  - Test your changes thoroughly.

- **Collaboration**:  
  Be respectful and constructive in all discussions. If you have any questions or need clarifications, please open an issue or join our discussions.

By contributing to this project, you agree to follow these guidelines. This helps maintain a secure, high-quality, and collaborative development environment.

Thank you for your contributions and happy coding!
