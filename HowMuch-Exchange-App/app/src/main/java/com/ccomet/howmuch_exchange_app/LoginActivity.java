package com.ccomet.howmuch_exchange_app;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class LoginActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        LoginDialog loginDialog = new LoginDialog();
        loginDialog.showDialog(LoginActivity.this);
    }
}
