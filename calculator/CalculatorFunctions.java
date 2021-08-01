package com.example.calculator;

public class CalculatorFunctions {


    String add (double n1, double n2)
    {
        return Double.toString(n1+n2);
    }
    String minus (double n1, double n2)
    {
        return Double.toString(n1-n2);
    }
    String multiply (double n1, double n2)
    {
        return Double.toString(n1*n2);
    }
    String divide (double n1, double n2)
    {   if(n2==0)return "ZeroDivsion error";
        return Double.toString(n1/n2);
    }
    String modulas (double n1, double n2)
    {   if(n2==0)return "ZeroDivsion error";
        return Double.toString(n1%n2);
    }
    String factorial (double n1)

    {   long ans=1;
        if(n1 ==(int)Math.round(n1))
       {
           while(n1>0)
           {
               ans *= n1;
               n1 = n1-1;
           }
       }
        else return "error";

        return Long.toString(ans);


    }


    String operator_selector(double n1, double n2, char c)
    {
        String ans="";


        switch (c)
        {
            case '+': ans = add(n1,n2);break;
            case '-': ans = minus(n1,n2);break;
            case 'X': ans = multiply(n1,n2);break;
            case '/': ans = divide (n1,n2);break;
            case '%': ans = modulas (n1,n2);break;
            case '!': ans = factorial (n1);break;
            default:break;
        }


        return ans;

    }


    String string_to_int(String s)
    {
        String ans="";
        StringBuilder s1= new StringBuilder();
        StringBuilder s2= new StringBuilder();
        double n1,n2;
        int i;
        char c ='0';
        boolean flag=true;

        for(i=0;i<s.length();i++)
        {
            if(flag&&(s.charAt(i)=='+'||s.charAt(i)=='-'||s.charAt(i)=='X'||s.charAt(i)=='/'||s.charAt(i)=='%'))
            {
                c = s.charAt(i);
                flag = false;
            }
            if (flag)
                s1.append(s.charAt(i));
            else
                s2.append(s.charAt(i));

        }
        n1 = Double.parseDouble(s1.toString());
        n2 = Double.parseDouble(s2.toString());
        ans = operator_selector(n1,n2,c);

        return ans;
    }
}
