package com.ccomet.howmuch_exchange_app;

import android.app.Activity;
import android.os.Bundle;

public class LoginActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        LoginDialog loginDialog = new LoginDialog();
        loginDialog.showDialog(LoginActivity.this);
    }
}
