from app import app


if __name__ == '__main__':
    # app.run(host='0.0.0.0') # PDR
    app.run(host="0.0.0.0", port=4000) # PDR
    # app.run(debug=True) # DEV
