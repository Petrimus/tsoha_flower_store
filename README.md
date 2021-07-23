# tsoha_flower_store
Helsinki University Course "tietokanta sovellus" 

## Intruduction
The application is online store where you can buy flowers. New customers have to redister to the system. Once that is done customers can sign in, navigate through product (that is flowers), add them in a temporary shopping cart and finally place an order. 

This application will not be complete online store. It will enable and concentrates to the functionality described above, but in comparison to fully working online store it omits some functionality. Inventory is used to check if there are enough products for order, but inventory is not changed after order, so it is some what static. Application does not include any payment methods and finally there will be no handling for placed orders aside that admin can update them as finished.

## Database
Database for developpment is a Postgres database running in a Docker container. 


## Features
- users can and must register to the system.
- users can log in.
- users can log out.
- users (and maybe everybody) can see a list of sellable products/flowers.
- logged users can add flowers to the shopping cart.
- logged users can remove flowers from shopping cart.
- logged user can see their current shopping cart. It will show flowers added and the sum price of the current shopping cart.
- logged users can place an order based on the current shopping cart.
- logged user can see his/her orders.
- admin can see orders.
- admin can filter orders by different variables.
- admin can delete orders.
- admin can change the status of the orders (in_progress, finishes, cancelled)  