
strings = ['https://www.dvo.com/newsletter/weekly/2014/05-09-115/w_images/hamburgers.jpg', 'https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/165384.jpg', 'https://images7.alphacoders.com/297/297530.jpg',
           'https://upload.wikimedia.org/wikipedia/commons/8/85/Hamburger_10000000041715_001080_(15637928889).jpg ', 'https://www.reddit.com/media?url=https%3A%2F%2Fexternal-preview.redd.it%2FXMilYCDdm9mlVE3RybHNzPAnNIw4kswfcP9Ad3PztcU.jpg%3Fauto%3Dwebp%26amp%3Bs%3D0fccbfd3d050330d185cb021d2ac8b8374f31382', 'http://3.bp.blogspot.com/_HPXWOvg7RcM/TSAlV0uVAnI/AAAAAAAAACo/kdGktUbFux8/s1600/burger.jpg', 'https://i2.wp.com/natashaskitchen.com/wp-content/uploads/2019/04/Best-Burger-5.jpg', 'http://static.businessinsider.com/image/530b5b696bb3f7421d5fdb47/image.jpg', 'https://www.inspiredtaste.net/wp-content/uploads/2016/08/Easy-Homemade-Hamburger-Recipe-1-1200.jpg']


for string in strings:
    print(string)
    if not 'reddit' in string:
        print(f'STRING: {string}\n')
