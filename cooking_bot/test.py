with open('pic.jpg', 'bw') as f:
    for chunk in r.iter_content(8192):
        f.write(chunk)