##  :page_facing_up: Instalación y uso 

###  :one: Run all tests: 
>Run Test :
```
    python3 test_shopping_cart.py
```

### :two: Generate Report
#### Install coverage
```
    python3 install coverage 
```
#### Generate Report by Console
>Run tests
```
   coverage run test_shopping_cart.py
```
> Generate report
```
   coverate report -m shopping_cart.py
```
#### Generate HTML Report
>Run tests
```
   coverage run test_shopping_cart.py
```
> Generate report
```
   coverate html shopping_cart.py
```
> Run server
```
   python3 -m http.server
```