from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


restaurants = {
    "1": {
        "Id": "1",
        "Name": "Holy Shnitzel",
        "Address": "654 Amsterdam Avenue",
        "Image": "https://yeahthatskosher.com/wp-content/uploads/2019/01/Holy-Schnitzel-Manhattan-NYC-Kosher-Restaurant4-1.jpg",
        "Popular Menu Items": ["Chicken Sandwiches", "Burgers"],  
        "Rating": 4,
        "Price Level": "Relatively Inexpensive",
        "Similair Restaurants": [4, 2],
        "Restaurant Blurb": "Holy Shnitzel is a kosher fast food restaurant specializing in schnitzel sandwiches with their famous sauces. Indoor seating is available and Uber Eats delivery is available online. Our restaurant is under kosher supervision. Our hours are from 10 am to 10 pm Sunday - Friday."
    },
    "2":{
        "Id": "2",
        "Name": "Noi Due Cafe",
        "Address": "143 West 69th Street",
        "Image": "https://lh3.googleusercontent.com/p/AF1QipO6wV8hXuMbC83jBJxnTJdA5tcVvGyJu06gjjHR=s1360-w1360-h1020",
        "Popular Menu Items": ["Pasta Carbonara", "Margherita Pizza", "Tiramisu"],
        "Rating": 5,
        "Price Level": "Affordable",
        "Similair Restaurants": [5, 1, 9],
        "Restaurant Blurb": "Noi Due Cafe offers authentic Italian cuisine in the heart of the Upper West Side. Enjoy our delicious pasta dishes, wood-fired pizzas, and decadent desserts. Our cozy atmosphere and friendly staff make it the perfect spot for a romantic dinner or casual meal with friends. We are open for lunch and dinner every day of the week."
    },
    "3":{
        "Id": "3",
        "Name": "Deli Kasbah",
        "Address": "251 West 85th Street",
        "Image": "https://lh3.googleusercontent.com/p/AF1QipPqWdLUSALQBAV-rMIUVRB5EmysQGahQiYEtat6=s1360-w1360-h1020",
        "Popular Menu Items": ["Shawarma Platter", "Falafel Wrap", "Baklava"],
        "Rating": 5,
        "Price Level": "Affordable",
        "Similair Restaurants": [4,7],
        "Restaurant Blurb": "Deli Kasbah offers a taste of the Mediterranean with our delicious Middle Eastern and Moroccan cuisine. From savory shawarma platters to fresh falafel wraps, our menu has something for everyone. Come experience the flavors of Morocco in the heart of the Upper West Side."
    },
    "4":{
        "Id": "4",
        "Name": "Saba's Pizza",
        "Address": "620 Amsterdam Avenue",
        "Image": "https://images.squarespace-cdn.com/content/v1/54ef7974e4b0b86cc0e9f609/1447691697739-DF0VX8BGD463R4W7BAM1/IMG_5534+%282%29.JPG",
        "Popular Menu Items": ["Grandma Slice", "Margherita Pizza", "Garlic Knots"],
        "Rating": 4,
        "Price Level": "Relatively Inexpensive",
        "Similair Restaurants": [1,6,8],
        "Restaurant Blurb": "Saba's Pizza is a neighborhood favorite known for our delicious New York-style pizzas and classic Italian dishes. Whether you're craving a slice of pepperoni pizza or a plate of spaghetti and meatballs, we've got you covered. Come enjoy a taste of Italy at Saba's Pizza!"
    },
    "5":{
        "Id": "5",
        "Name": "Amsterdam Burger",
        "Address": "428 Amsterdam Avenue",
        "Image": "https://lh3.googleusercontent.com/p/AF1QipN9de64K6y34mXfxr4IaTG1JhxzbIxG3ECpJTCp=s1360-w1360-h1020",
        "Popular Menu Items": ["Classic Burger", "BBQ Bacon Burger", "Truffle Fries"],
        "Rating": 4,
        "Price Level": "Affordable",
        "Similair Restaurants": [6, 3],
        "Restaurant Blurb": "Amsterdam Burger is your destination for mouthwatering burgers made with premium ingredients. From our classic burgers to our specialty creations, each bite is a burst of flavor. Pair your burger with our signature truffle fries for the ultimate dining experience."
    },
    "6":{
        "Id": "6",
        "Name": "Carlos and Gabby's",
        "Address": "688 Amsterdam Avenue",
        "Image": "https://d1ralsognjng37.cloudfront.net/3fb1636b-603a-4167-84d9-bafa96e28fd2",
        "Popular Menu Items": ["Fajita Burrito", "Grilled Chicken Salad", "Churros"],
        "Rating": 4,
        "Price Level": "Relatively Inexpensive",
        "Similair Restaurants": [7, 1],
        "Restaurant Blurb": "Carlos and Gabby's offers a unique blend of Mexican and American cuisine with a kosher twist. From sizzling fajitas to crispy tacos, our menu is full of flavorful dishes that will satisfy your cravings. Join us for a delicious meal in a vibrant and welcoming atmosphere."
    },
    "7":{
        "Id": "7",
        "Name": "Bagels and Co",
        "Address": "370 Amsterdam Avenue",
        "Image": "https://s3-media0.fl.yelpcdn.com/bphoto/vJFkdxpgSf1ciPP4zqmDUw/348s.jpg",
        "Popular Menu Items": ["Everything Bagel", "Nova Lox Sandwich", "Cheesecake"],
        "Rating": 3,
        "Price Level": "Relatively Inexpensive",
        "Similair Restaurants": [2, 10],
        "Restaurant Blurb": "Bagels and Co is a cozy kosher deli known for our freshly baked bagels and delicious sandwiches. Whether you're craving a classic everything bagel or a hearty Nova lox sandwich, we've got you covered. Join us for breakfast, lunch, or dinner and experience the taste of New York's finest bagels."
    },
    "8": {
        "Id": "8",
        "Name": "Izzy's Steakhouse",
        "Address": "354 Amsterdam Avenue",
        "Image": "https://izzyssmokehouse.com/images/izzy-bbq-smokehouse-brisket-on-tray.jpg",
        "Popular Menu Items": ["Ribeye Steak", "Filet Mignon", "Garlic Mashed Potatoes"],
        "Rating": 3,
        "Price Level": "Affordable",
        "Similair Restaurants": [4, 3],
        "Restaurant Blurb": "Izzy's Steakhouse is a premier kosher steakhouse offering the finest cuts of meat and exquisite dining experience. From our juicy ribeye steaks to our tender filet mignon, each dish is prepared to perfection. Join us for an unforgettable meal in an elegant and upscale setting."
    },
    "9": {
        "Id": "9",
        "Name": "Mexikosher",
        "Address": "100 West 83rd Street",
        "Image": "https://images.squarespace-cdn.com/content/v1/5c5b1b77755be219a9e4dc2e/1587415778322-ROCT335TISPV0CUL94C7/Mexikosher_BuildYourTacos_native.JPG",
        "Popular Menu Items": ["Tacos al Pastor", "Quesadillas", "Churros"],
        "Rating": 4,
        "Price Level": "Affordable",
        "Similair Restaurants": [8, 7, 10],
        "Restaurant Blurb": "Mexikosher brings the flavors of Mexico to the kosher dining scene. From our savory tacos al pastor to our cheesy quesadillas, every bite is a fiesta of flavors. Join us for a culinary journey through Mexico in a kosher-friendly environment."
    },
    "10":{
        "Id": "10",
        "Name": "Noi Due Carne",
        "Address": "691 Amsterdam Avenue",
        "Image": "https://images.getbento.com/accounts/928d2470201bbd905280be77bd37733a/media/images/65677Noi_Due_Carne_0919_.jpg?w=1200&fit=crop&auto=compress,format&h=600",
        "Popular Menu Items": ["Filet Mignon", "Rack of Lamb", "Tiramisu"],
        "Rating": 5,
        "Price Level": "Premium",
        "Similair Restaurants": [],
        "Restaurant Blurb": "Noi Due Carne offers a sophisticated dining experience with an emphasis on premium meats and Italian specialties. From our succulent filet mignon to our tender rack of lamb, each dish is a celebration of flavor and craftsmanship. Indulge in our delectable desserts and extensive wine list for an unforgettable meal."
    }

}

# ROUTES

@app.route('/')
def welcome():
   global restaurants
   return render_template('home.html',restaurants=restaurants)  

@app.route('/add-restaurant')
def add():
    return render_template('add.html')




@app.route('/add_rest', methods=['POST'])
def add_rest():
    global restaurants  

    json_data = request.get_json()
    
    new_id = str(len(restaurants) + 1)

    newRest = {
        "Id": len(restaurants) + 1,
        "Name": json_data["Name"],
        "Address": json_data["Address"],
        "Image": json_data["ImageLink"],
        "Popular Menu Items": json_data["PopularItems"],
        "Price Level": json_data["Price"],
        "Rating": json_data["Rating"],
        "Restaurant Blurb": json_data["Blurb"],
        "Similair Restaurants": [],

    }
    restaurants[new_id] = newRest    

    return jsonify({'message': 'Restaurant added successfully', 'Id': newRest["Id"]})

@app.route('/update_rest/<num>', methods=['PUT']) 
def update(num=None):
    global restaurants
    json_data = request.get_json()

    restaurants[num]["Name"] = json_data["Name"]
    restaurants[num]["Address"] = json_data["Address"]
    restaurants[num]["Image"] = json_data["ImageLink"]
    restaurants[num]["Popular Menu Items"] = json_data["PopularItems"]
    restaurants[num]["Price Level"] = json_data["Price"]
    restaurants[num]["Rating"] = json_data["Rating"]
    restaurants[num]["Restaurant Blurb"] = json_data["Blurb"]


    return jsonify({'message': 'Restaurant added successfully'})




@app.route('/view/<num>')
def hello_world(num=None):
   global restaurants
   restaurant = restaurants[num]
   return render_template('view.html', restaurant=restaurant, restaurants=restaurants)   

@app.route('/get-directions/<num>')
def get_d(num=None):
    global restaurants
    restaurant = restaurants[num]
    return render_template('get_d.html', restaurant=restaurant, restaurants=restaurants)


@app.route('/edit/<num>')
def edit_data(num=None):
   global restaurants
   restaurant = restaurants[num]
   return render_template('edit.html', restaurant=restaurant)   




@app.route('/search_results/<input>')
def search(input=None):
    global restaurants
    results = []
    blurbs = []
    price = []
    for key, value in restaurants.items():
        if input.lower() in value["Name"].lower():
            results.append(restaurants[key])

        if input.lower() in value["Restaurant Blurb"].lower():
            blurbs.append(restaurants[key])
        
        if input.lower() in value["Price Level"].lower():
            price.append(restaurants[key])

    return render_template('search.html', price=price, blurbs=blurbs, results=results, input=input)  




if __name__ == '__main__':
   app.run(debug = True)


