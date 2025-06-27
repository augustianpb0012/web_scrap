from app import create_app

app = create_app()

try:
    if __name__ == "__main__":
        app.run(debug=True)
        print("App is running...")
except Exception as e:
    print(f"Error while starting the Flask app: {e}")
