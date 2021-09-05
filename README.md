# tsoha_flower_store
Helsinki University Course "tietokantasovellus harjoitus"

## Final version

Application is running on [Heroku](https://tsoha-flower-store.herokuapp.com/). You can test it with user username test@tester.io and password testing10. All features described later are implemented. Test user is only one with admin priviledges. Little unintuitively test user is also customer.
 
## Introduction
The application is an online store where you can buy flowers. New customers have to register to the system. Once that is done customers can sign in, navigate through products (that is flowers), add them in a temporary shopping cart and finally place an order.
 
This application will not be a complete online store. It will enable and concentrate on the functionality described above, but in comparison to fully working online stores it omits some functionality. Inventory is used to check if there are enough products for order, but inventory is not changed after order, so it is somewhat static. Application does not include any payment methods and finally there will be no handling for placed orders aside that admin can update them as finished.
 
## Database
Database for development is a Postgres database running in a Docker container and orchestrated with docker-compose. You can start a prefilled database by command ```docker-compose up``` in the project root. You have to have docker-compose installed in your machine.
 
Database has eight tables:
- flower_user lists all the users including admin user/users.
- adress
- flower will contain product information.
- inventory shows how many flowers there are currently in the inventory.
- shoppingcart is the current order. It can have different statuses.
- shoppingcart_item one product/flower in the shopping cart.
- shoppingcart_status are the different statuses a shopping cart can have. I don't know if this table is a good idea, but we will see that later.
 
 
## Features
- users can and must register to the system.
- users can log in.
- users can log out. 
- users (and everybody) can see a list of sellable products/flowers.
- logged users can add flowers to the shopping cart.
- logged users can remove flowers from the shopping cart.
- logged users can see their current shopping cart. It will show flowers added and the sum price of the current shopping cart.
- logged users can place an order based on the current shopping cart.
- logged user can see his/her orders.
- admin can see orders. 
- admin can see users.
