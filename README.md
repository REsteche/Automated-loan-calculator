# Automated loan calculator project from JetBrains

One of the first Python Education projects that i have done in JetBrains Plataform while learning the fundamentals of the language. Here, you can find the scope of each file divided into the subfolders of that repository.


## Description - Stage 2: the Dreamworld
The user might know the period of the loan and want to calculate the monthly payment. Or the user might know the amount of the monthly repayments and wonder how many months it will take to repay the loan in full.
We need to ask the user to input the loan principal amount. Then, the user should indicate what needs to be calculated (the monthly payment amount or the number of months) and enter the required parameter. After that, the loan calculator should output the value that the user wants to know.
Also, let’s assume we don't care about decimal places. If you get a floating-point expression as a result of the calculation, you’ll have to do additional actions. Take a look at Example 4 where you need to calculate the monthly payment. You know that the loan principal is 1000 and want to pay it back in 9 months. The real value of payment can be calculated as:

_payment_ = _principal_/_months_ = 1000/9 = 111.11...

Of course, you can’t pay that amount of money. You have to round up this value and make it 112. Remember that no payment can be more than the fixed monthly payment. If your monthly repayment amount is 111, that would make the last payment 112, which is not acceptable. If you make a monthly payment of 112, the last payment will be 104, which is fine. You can calculate the last payment as follows:

_lastpayment_ = _principal_-(_periods_-1)*_payment_ = 1000-8*112 = 104

In this stage, you need to count the number of months or the monthly payment. If the last payment differs from the rest, the program should display the monthly payment and the last payment.

## Objectives
The behavior of your program should look like this:
* Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount.
* To perform further calculations, you'll also have to ask for the required missing value.
* Finally, output the results for the user.


## Description  - Stage 3: the Annuity Payment
Let's compute all the parameters of the loan. There are at least two kinds of loan: those with annuity payment and those with differentiated payment. In this stage, you are going to calculate only the annuity payment which is fixed during the whole loan term.
Where:
* A = annuity payment;
* p = loan principal;
* i = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage. For example, if your annual interest rate = 12%, then i = 0.01;
* n = number of payments. This is usually the number of months in which repayments will be made.

The explicit formula should perform like: 

A = P*(i* (1 + i)^n)/((1 + i)^n - 1)

You are interested in four values: the number of monthly payments required to repay the loan, the monthly payment amount, the loan principal, and the loan interest.

## Objectives
In this stage, you should add new behavior to the calculator:
1 - First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.
2 - Then, you need to ask them to input the remaining values.
3 - Finally, compute and output the value that they wanted.

__Note that the user inputs the interest rate as a percentage, for example, 11.7, so you should divide this value by 100 to use it in the formula above.
Please be careful converting "_X months_" to "_Y years and Z months_". Avoid writing "_0 years and 11 months_" (output "_11 months_" instead) and "_1 years and 0 months_" (output "_1 year_" instead).__

Note that in this stage, you have to ask the user to input parameters in a specific order which is provided below. Simply skip the value the user wants to calculate:

* The first is the loan principal.
* The second is the monthly payment.
* The next is the number of monthly payments.
* The last is the loan interest.

## Description - Stage 4: Differentiate payment
Finally, let's add to our calculator the capacity to compute differentiated payments. We’ll do this for the type of repayment where the loan principal is reduced by a constant amount each month. The rest of the monthly payment goes toward interest repayment and it is gradually reduced over the term of the loan. This means that the payment is different each month. 

* P = the loan principal;
* i = nominal interest rate. This is usually 1/12 of the annual interest rate, and it’s usually a float value, not a percentage. For example, if our annual interest rate = 12%, then i = 0.01.
* n = number of payments. This is usually the number of months in which repayments will be made.
* m = current repayment month.
* 
The user has to input a lot of parameters, so it might be convenient to use command-line arguments.
You can run your loan calculator via command line like this:


`
python loan_calc_{stage}.py
`

## Objectives 

In this stage, the following features are going to be implemente to the project:

* Calculation of differentiated payments. To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.
* Ability to calculate the same values as in the previous stage for annuity payment (principal, number of monthly payments, and monthly payment amount). The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.
* Handling of invalid parameters. It's a good idea to show an error message if the user enters invalid parameters (they are discussed in detail below).

The final version of your program is supposed to work from the command line and parse the following parameters.
* ` --type `
* ` --payment `
* ` --principal `
* ` --periods `
* ` --interest `

