from app import app

if __name__ == '__main__':
    # Threaded = False prevents GDrive API calls from bugging out
    app.run(debug=True)
    # app.run(debug=True, threaded=False)
