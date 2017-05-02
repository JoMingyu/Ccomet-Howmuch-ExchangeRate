package com.ccomet.howmuch_exchange_app;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.Toast;

import com.facebook.CallbackManager;
import com.facebook.FacebookCallback;
import com.facebook.FacebookException;
import com.facebook.FacebookSdk;
import com.facebook.GraphRequest;
import com.facebook.GraphResponse;
import com.facebook.login.LoginResult;
import com.facebook.login.widget.*;
import com.facebook.login.widget.LoginButton;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.Arrays;
import java.util.List;

public class LoginOverlayActivity extends Activity {

    Button registerButton;
    Button facebookStartButton;
    Button googleStartButton;
    LinearLayout noLoginButton;

    com.facebook.login.widget.LoginButton loginButton;
    CallbackManager callbackManager;

    String name, email, gender;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        FacebookSdk.sdkInitialize(this.getApplicationContext());
        setContentView(R.layout.activity_login_overlay);

        WindowManager.LayoutParams params = getWindow().getAttributes();
        params.width = WindowManager.LayoutParams.MATCH_PARENT;
        params.height = WindowManager.LayoutParams.MATCH_PARENT;
        getWindow().setAttributes(params);
        getWindow().setBackgroundDrawable(new ColorDrawable(Color.TRANSPARENT));

        registerButton = (Button)findViewById(R.id.register_button);
        facebookStartButton = (Button)findViewById(R.id.facebook_start_button);
        googleStartButton = (Button)findViewById(R.id.google_start_button);
        noLoginButton = (LinearLayout)findViewById(R.id.no_login_button);

        registerButton.setOnClickListener(onClickListener);
        facebookStartButton.setOnClickListener(onClickListener);
        googleStartButton.setOnClickListener(onClickListener);
        noLoginButton.setOnClickListener(onClickListener);

        callbackManager = CallbackManager.Factory.create();
        loginButton = (LoginButton)findViewById(R.id.facebook_login_button);

        callbackManager = CallbackManager.Factory.create();

        loginButton.setReadPermissions(Arrays.asList("public_profile", "email"));
        loginButton.registerCallback(callbackManager, new FacebookCallback<LoginResult>() {
            @Override
            public void onSuccess(LoginResult loginResult) {
                GraphRequest graphRequest = GraphRequest.newMeRequest(loginResult.getAccessToken(), new GraphRequest.GraphJSONObjectCallback() {
                    @Override
                    public void onCompleted(JSONObject object, GraphResponse response) {
                        Log.v("result", object.toString());
                    }
                });

                Bundle parameters = new Bundle();
                parameters.putString("fields", "id,name,email,gender,birthday");
                graphRequest.setParameters(parameters);
                graphRequest.executeAsync();
            }

            @Override
            public void onCancel() {
                System.out.println("onCancel");
            }

            @Override
            public void onError(FacebookException error) {
                System.out.println("onError");
            }
        });

        /*
        List<String> permissionNeeds = Arrays.asList("public_profile", "email", "AccessToken");
        loginButton.registerCallback(callbackManager, new FacebookCallback<LoginResult>() {
            @Override
            public void onSuccess(LoginResult loginResult) {
                System.out.println("onSuccess");
                String accessToken = loginResult.getAccessToken().getToken();
                Log.d("Access Token", accessToken);

                GraphRequest request = GraphRequest.newMeRequest(
                        loginResult.getAccessToken(), new GraphRequest.GraphJSONObjectCallback() {
                            @Override
                            public void onCompleted(JSONObject object, GraphResponse response) {
                                Log.d("Login Activity", response.toString());
                                try {
                                    name = object.getString("name");
                                    email = object.getString("email");
                                    gender = object.getString("gender");
                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }
                            }
                        }
                );

                Bundle parameters = new Bundle();
                parameters.putString("fields", "id,name,email,gender,birthday");
                request.setParameters(parameters);
                request.executeAsync();
            }

            @Override
            public void onCancel() {
                System.out.println("onCancel");
            }

            @Override
            public void onError(FacebookException error) {
                System.out.println("onError");
            }
        });
        */
    }

    View.OnClickListener onClickListener = new View.OnClickListener(){
        @Override
        public void onClick(View v){
            switch(v.getId()){
                case R.id.register_button:
                    Toast.makeText(LoginOverlayActivity.this, "register Button Clicked", Toast.LENGTH_SHORT).show();
                    break;
                case R.id.facebook_start_button:
                    Toast.makeText(LoginOverlayActivity.this, "facebook start Button Clicked", Toast.LENGTH_SHORT).show();
                    loginButton.performClick();
                    break;
                case R.id.google_start_button:
                    Toast.makeText(LoginOverlayActivity.this, "google+ start Button Clicked", Toast.LENGTH_SHORT).show();
                    break;
                case R.id.no_login_button:
                    Toast.makeText(LoginOverlayActivity.this, "Start with no sign in Button Clicked", Toast.LENGTH_SHORT).show();
                    break;
                default:
                    break;
            }
        }
    };

    @Override
    protected void onActivityResult(int requestCode, int responseCode, Intent data){
        super.onActivityResult(requestCode, responseCode, data);
        callbackManager.onActivityResult(requestCode, responseCode, data);
    }
}
