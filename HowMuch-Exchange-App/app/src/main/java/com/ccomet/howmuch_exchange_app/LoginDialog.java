package com.ccomet.howmuch_exchange_app;

import android.app.Dialog;
import android.content.Context;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.Toast;

/**
 * Created by 20311Leesoomin on 2017-03-30.
 */

public class LoginDialog {

    private Dialog dialog;

    private Button registerButton;
    private Button facebookStartButton;
    private Button googleStartButton;
    private LinearLayout noLoginButton;     //Use LinearLayout like Button

    private Context loginActivityContext;

    public void showDialog(final Context context) {
        loginActivityContext = context;

        //Dialog setup
        dialog = new Dialog(context);
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE);
        dialog.setContentView(R.layout.logindialog);
        dialog.setCancelable(true); //이 속성이 무엇인지 확인 바람

        WindowManager.LayoutParams params = dialog.getWindow().getAttributes();
        params.width = WindowManager.LayoutParams.MATCH_PARENT;
        params.height = WindowManager.LayoutParams.MATCH_PARENT;
        dialog.getWindow().setAttributes(params);
        dialog.getWindow().setBackgroundDrawable(new ColorDrawable(Color.TRANSPARENT));

        dialog.show();

        registerButton = (Button) dialog.findViewById(R.id.register_button);
        facebookStartButton = (Button)dialog.findViewById(R.id.facebook_start_button);
        googleStartButton = (Button)dialog.findViewById(R.id.google_start_button);
        noLoginButton = (LinearLayout)dialog.findViewById(R.id.no_login_button);

        registerButton.setOnClickListener(onClickListener);
        facebookStartButton.setOnClickListener(onClickListener);
        googleStartButton.setOnClickListener(onClickListener);
        noLoginButton.setOnClickListener(onClickListener);
    }

    View.OnClickListener onClickListener = new View.OnClickListener(){
        @Override
        public void onClick(View v){
            switch(v.getId()){
                case R.id.register_button:
                    Toast.makeText(loginActivityContext, "register Button Clicked", Toast.LENGTH_SHORT).show();
                    break;
                case R.id.facebook_start_button:
                    Toast.makeText(loginActivityContext, "facebook start Button Clicked", Toast.LENGTH_SHORT).show();
                    break;
                case R.id.google_start_button:
                    Toast.makeText(loginActivityContext, "google+ start Button Clicked", Toast.LENGTH_SHORT).show();
                    break;
                case R.id.no_login_button:
                    Toast.makeText(loginActivityContext, "Start with no sign in Button Clicked", Toast.LENGTH_SHORT).show();
                    break;
                default:
                    break;
            }
        }
    };

}
