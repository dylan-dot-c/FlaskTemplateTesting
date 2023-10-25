# Flask Template With Bootstrap

This is a simple scaffold template to help you get started with Flask applications quickly.

**Note:** This template is not recommended for beginners, as it assumes prior knowledge of Flask.



## Getting Started

To use this template in your project, follow these steps:

1. Click the "Use This Template" button and create a new repository on GitHub.

2. On the new repository page, provide a name for your project and create it.

3. Copy the URL of your newly created GitHub repository and open your project folder in Visual Studio Code (assuming you've already created one).

4. Clone the repository locally using the following command:

   ```sh
   git clone <repository_url>
   ```

5. After cloning the repo, create a virtual environment. The process may differ between Windows and macOS:

   - **Windows**:
     ```sh
     python -m venv venv
     ```

   - **macOS**:
     ```sh
     python3 -m venv venv
     ```

6. Activate the virtual environment. On Windows, use:

   ```sh
   venv\Scripts\activate
   ```

   On macOS, you can activate the virtual environment using a command similar to the Windows one. The command should be something like:

   ```sh
   source venv/bin/activate
   ```

7. With your virtual environment activated, install the project dependencies from `requirements.txt`:

   ```sh
   pip install -r requirements.txt
   ```

8. Ensure that your active interpreter in Visual Studio Code is set to ('venv':venv). You can check and change it by opening a .py file and locating the interpreter option in the bottom-right corner of Visual Studio Code.

9. Now that everything should be set up correctly, run your Flask application with the following command:

   ```sh
   flask run --debug
   ```

   If you want to specify a different port, you can use the `-p` option, like this:

   ```sh
   flask run --debug -p 8080
   ```

10. Thanks for using this template! Happy FlaskStrapping!

## About This Template

This template provides two routes:

- **Index**: The default route.
- **Contact**: A route that uses a WTF form for contact information.

Feel free to customize and build your Flask application upon this template.

Please let me know if you need any further assistance or have any questions!

##Pages
![Home Page Preview](https://github.com/dylan-dot-c/Flask-Todo-App/blob/main/flaskHome.png?raw=true)
![Home Page Preview](https://github.com/dylan-dot-c/Flask-Todo-App/blob/main/contactPage.png?raw=true)
