package com.example.calculator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    String s = "";

   private TextView input_calc;
    public String removeLastChar(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        return s.substring(0, s.length()-1);

    }

    CalculatorFunctions calculatorFunctions = new CalculatorFunctions();

    @Override
    public void onClick(View view) {

        switch (view.getId())
        {
            case R.id.button0:s+= "0";input_calc.setText(s);break;
            case R.id.button1:s+= "1";input_calc.setText(s);break;
            case R.id.button2:s+= "2";input_calc.setText(s);break;
            case R.id.button3:s+= "3";input_calc.setText(s);break;
            case R.id.button4:s+= "4";input_calc.setText(s);break;
            case R.id.button5:s+= "5";input_calc.setText(s);break;
            case R.id.button6:s+= "6";input_calc.setText(s);break;
            case R.id.button7:s+= "7";input_calc.setText(s);break;
            case R.id.button8:s+= "8";input_calc.setText(s);break;
            case R.id.button9:s+= "9";input_calc.setText(s);break;
            case R.id.buttonpoint:s+= ".";input_calc.setText(s);break;
            case R.id.buttonplus:s+= "+";input_calc.setText(s);break;
            case R.id.buttonminus:s+= "-";input_calc.setText(s);break;
            case R.id.buttonmultiply:s+= "X";input_calc.setText(s);break;
            case R.id.buttondivide:s+= "/";input_calc.setText(s);break;
            case R.id.buttonmodulas:s+= "%";input_calc.setText(s);break;
            case R.id.buttonsquare:input_calc.setText(s);break;
            case R.id.buttonAC:s="";input_calc.setText(s);break;
            case R.id.buttonback:s = removeLastChar(s);input_calc.setText(s);break;
            case R.id.buttonequal:s= calculatorFunctions.string_to_int(s);input_calc.setText(s);break;
            default:break;
        }

    }



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        input_calc = findViewById(R.id.input);
        Button button0 = findViewById(R.id.button0);
        button0.setOnClickListener(this);
        Button button1 = findViewById(R.id.button1);
        button1.setOnClickListener(this);
        Button button2 = findViewById(R.id.button2);
        button2.setOnClickListener(this);
        Button button3 = findViewById(R.id.button3);
        button3.setOnClickListener(this);
        Button button4 = findViewById(R.id.button4);
        button4.setOnClickListener(this);
        Button button5 = findViewById(R.id.button5);
        button5.setOnClickListener(this);
        Button button6 = findViewById(R.id.button6);
        button6.setOnClickListener(this);
        Button button7 = findViewById(R.id.button7);
        button7.setOnClickListener(this);
        Button button8 = findViewById(R.id.button8);
        button8.setOnClickListener(this);
        Button button9 = findViewById(R.id.button9);
        button9.setOnClickListener(this);
        Button buttonpoint = findViewById(R.id.buttonpoint);
        buttonpoint.setOnClickListener(this);
        Button buttonplus = findViewById(R.id.buttonplus);
        buttonplus.setOnClickListener(this);
        Button buttonminus = findViewById(R.id.buttonminus);
        buttonminus.setOnClickListener(this);
        Button buttonmultiply = findViewById(R.id.buttonmultiply);
        buttonmultiply.setOnClickListener(this);
        Button buttondivide = findViewById(R.id.buttondivide);
        buttondivide.setOnClickListener(this);
        Button buttonmodulas = findViewById(R.id.buttonmodulas);
        buttonmodulas.setOnClickListener(this);
        Button buttonsquare = findViewById(R.id.buttonsquare);
        buttonsquare.setOnClickListener(this);
        Button buttonAC = findViewById(R.id.buttonAC);
        buttonAC.setOnClickListener(this);
        Button buttonequal = findViewById(R.id.buttonequal);
        buttonequal.setOnClickListener(this);









    }


}