# sphinx-api-any

This is a very simple program that extracts content from source files into `rst` files. The goal is to be able to write documentation in rst format within the code. This __does not automatically__ parse the code, but allows developers to keep comments within the code and to use all the syntax of `sphinx`.

## initialising

start by creating a `doc` folder and initialize sphinx in it 

    mkdir doc
    cd doc
    sphinx-quickstart

follow the instructions. Then use sphinx-api-any to generate your rst files from the code. For example:

    sphinx-apy-any ../julia/ ./source/

and finally generate the html output using sphinx

    make html


## installation

very simple:

    pip install sphinx-api-any

## Example of sphinx formated code from my own project:


    #' .. py:function:: solve(M,p)
    #'    Solves a model constructed using the Model and Parameter objects. It updates the model with
    #'    the solution.
    function solve(M::Model , p::Param)
      # extract relevaant 
      H   = M.H; S=M.S; U=M.U; P0=M.P0; G= M.G; Z = M.Z; V = M.V; B = M.B; F=M.F; I0= M.I0; W0 = M.W0;
      kp  = 0.1;


# Links

 - [Sphinx markup language](http://sphinx-doc.org/domains.html#the-c-domain)
 - [Sphinx tutorial](http://sphinx-doc.org/tutorial.html)

# Todos

 - allow to automatically include the raw code inside the documentation
 - if some lines do match some regular expression, generate some sphinx rst directives
 - get options from config file, pass them as argument