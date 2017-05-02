package com.ccomet.howmuch_exchange_app;

import android.content.Context;
import android.content.res.TypedArray;
import android.util.AttributeSet;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

/**
 * Created by 20311Leesoomin on 2017-03-29.
 */

public class LoginButton extends LinearLayout{
    LinearLayout bg;
    ImageView symbol;
    TextView text;

    public LoginButton(Context context){
        super(context);
        initView();
    }

    public LoginButton(Context context, AttributeSet attrs){
        super(context, attrs);
        initView();
        getAttrs(attrs);
    }

    public LoginButton(Context context, AttributeSet attrs, int defStyle){
        super(context, attrs);
        initView();
        getAttrs(attrs, defStyle);
    }

    private void initView(){
        String infService = Context.LAYOUT_INFLATER_SERVICE;
        LayoutInflater layoutInflater = (LayoutInflater)getContext().getSystemService(infService);
        View v = layoutInflater.inflate(R.layout.login_activity_buttons_view, this, false);
        addView(v);

        bg = (LinearLayout)findViewById(R.id.bg);
        symbol = (ImageView)findViewById(R.id.symbol);
        text = (TextView)findViewById(R.id.text);
    }

    private void getAttrs(AttributeSet attrs){
        TypedArray typedArray = getContext().obtainStyledAttributes(attrs, R.styleable.LoginButton);
        setTypeArray(typedArray);
    }

    private void getAttrs(AttributeSet attrs, int defStyle){
        TypedArray typedArray = getContext().obtainStyledAttributes(attrs, R.styleable.LoginButton, defStyle, 0);
        setTypeArray(typedArray);
    }

    private void setTypeArray(TypedArray typedArray){
        int bg_resID = typedArray.getResourceId(R.styleable.LoginButton_bg, R.drawable.register);
        bg.setBackgroundResource(bg_resID);

        int symbol_resID = typedArray.getResourceId(R.styleable.LoginButton_bg, R.mipmap.ic_launcher);
        symbol.setImageResource(symbol_resID);

        int textColor = typedArray.getColor(R.styleable.LoginButton_textColor, 0);
        text.setTextColor(textColor);

        String textString = typedArray.getString(R.styleable.LoginButton_text);
        text.setText(textString);

        typedArray.recycle();
    }

    void setBg(int bg_resID){
        bg.setBackgroundResource(bg_resID);
    }

    void setSymbol(int symbol_resID){
        symbol.setImageResource(symbol_resID);
    }

    void setTextColor(int color){
        text.setTextColor(color);
    }

    void setText(String textString) {
        text.setText(textString);
    }

    void setText(int text_resID){
        text.setText(text_resID);
    }
}
