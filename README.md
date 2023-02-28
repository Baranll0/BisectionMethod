<h1>Numerical Analysis</h1>
<h2>What is Bisection Method?</h2>
<p>The bisection method is one of the implicit methods used to find roots. An attempt is made to find the root with a lower and upper value containing the root. If the value of a function changes from - to + or from + to -, then that function value becomes zero at some point in this transition.</p>
<hr>
<h3>What did I do in this app?</h3>
<p>
    <pre>We perform the root of the equation 𝑥**3 − 2*(x**2) − 5 = 0 in the interval [2,4] with the method in 4 iterations.</pre>
    <pre> x**3 +4*(x**2)-10=0 in the interval [1,2] until the margin of error relative to the solution is ε = 10**-6 by the method of dividing the root by two we will continue.</pre>
</p>
<hr>
<h3> Tech I use: </h3>
<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" width="50" height="50"/>
<hr>
<h3>Modules I use: </h3>
<img src="https://img.shields.io/badge/math-%2320232a.svg?style=for-the-badge&logo=math&logoColor=blue"/>
<hr>
<p><h4>Declaration:</h4>
   <pre>
      -Let's define a function for the equation.
      -Next, let's define the function of the Bisection method and code the algorithm of the Bisection method.
      -Then let's get the "lower range", "upper range" and "number of iterations" values from the user.
      -But there is one thing we should be careful about: the product of the value of the function in the lower range and the value of the function in the upper range        must be less than 0!
      -If it is less than zero, we can call the function.
  </pre>
  <pre>
      If we talk about the algorithm of the bisection method:
         -First we define an i variable value. This i value will be important for the loop we will use later.<br>
         -Then we define an x value and this x value will hold the value of (upper + lower)/2 in the bisection method. We set the value 0 at the beginning.<br>
         -We set the loop and x We update xi as =(lower range+upper range)/2.<br>
         -If the value of x in the function is less than zero, lower bound=x, otherwise upper bound=x.<br>
         -Then i for the loop to continue We increase its value.<br>
  </pre>
  
  I look forward to your ideas and thoughts. Enjoy your work!
