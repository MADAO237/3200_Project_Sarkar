CREATE DATABASE IF NOT EXISTS laundry_db;
USE laundry_db;


-- Customers Table
CREATE TABLE IF NOT EXISTS Customers (
    user_id   INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(100),
    lastName  VARCHAR(100),
    email     VARCHAR(100),
    address   TEXT
);

-- Laundromat Table
CREATE TABLE IF NOT EXISTS laundromats (
    laundromat_id INT AUTO_INCREMENT PRIMARY KEY,
    location      VARCHAR(100),
    pricing       INT,
    avg_rating    INT,
    delivery_fee  INT,
    coupon_rev    VARCHAR(7),
    num_orders    INT,
    time_process  INT 
);



-- Orders Table
CREATE TABLE IF NOT EXISTS orders (
    order_id          INT AUTO_INCREMENT PRIMARY KEY,
    user_id           INT,
    laundromat_id     INT,
    pickup_location   VARCHAR(100),
    delivery_location VARCHAR(100),
    pickup_time       DATETIME,
    delivery_time     DATETIME,
    total_cost        INT,
    status            TINYINT,
    promo_code        VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES Customers(user_id) ON DELETE CASCADE,
    FOREIGN KEY (laundromat_id) REFERENCES laundromats(laundromat_id) ON DELETE SET NULL
);

-- Order Details Table
CREATE TABLE IF NOT EXISTS OrderDetails (
    detail_id     INT AUTO_INCREMENT PRIMARY KEY,
    order_id      INT,
    order_date    DATETIME,
    delivery_date DATETIME,
    location      VARCHAR(100),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

-- Customer Reviews Table
CREATE TABLE IF NOT EXISTS CustomerReviews (
    review_id     INT AUTO_INCREMENT PRIMARY KEY,
    user_id       INT,
    laundromat_id INT,
    rating        INT,
    text          TEXT,
    title         TEXT,
    FOREIGN KEY (user_id) REFERENCES Customers(user_id) ON DELETE CASCADE,
    FOREIGN KEY (laundromat_id) REFERENCES laundromats(laundromat_id) ON DELETE CASCADE
);


-- Logs Table
CREATE TABLE IF NOT EXISTS Logs (
    logs_id     INT AUTO_INCREMENT PRIMARY KEY,
    event_type  VARCHAR(100),
    description TEXT,
    timestamp   DATETIME,
    user_id     INT,
    FOREIGN KEY (user_id) REFERENCES Customers(user_id) ON DELETE CASCADE
);

-- Locations Table
CREATE TABLE IF NOT EXISTS Locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id     INT,
    address     VARCHAR(100),
    label       VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES Customers(user_id) ON DELETE CASCADE
);







