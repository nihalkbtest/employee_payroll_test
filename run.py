from app import create_app

# Create the Flask app instance
app = create_app()

if __name__ == '__main__':
    # Run the app with debug mode enabled
    app.run(debug=True)
