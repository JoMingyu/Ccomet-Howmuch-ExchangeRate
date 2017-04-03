package com.ccomet.howmuch_exchange_app;

import android.content.Intent;
import android.hardware.camera2.params.Face;
import android.support.v4.app.FragmentActivity;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import com.facebook.AccessToken;
import com.facebook.FacebookSdk;
import com.google.android.gms.auth.api.Auth;
import com.google.android.gms.auth.api.signin.GoogleSignInAccount;
import com.google.android.gms.auth.api.signin.GoogleSignInOptions;
import com.google.android.gms.auth.api.signin.GoogleSignInResult;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.common.api.OptionalPendingResult;

public class LoginCheck extends FragmentActivity implements GoogleApiClient.OnConnectionFailedListener{

    GoogleApiClient mGoogleApiClient;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        FacebookSdk.sdkInitialize(LoginCheck.this);
        setContentView(R.layout.activity_login_check);

        GoogleSignInOptions gso = new GoogleSignInOptions.Builder(GoogleSignInOptions.DEFAULT_SIGN_IN).requestEmail().build();

        mGoogleApiClient = new GoogleApiClient.Builder(this)
                .enableAutoManage(this /*FragmentActivity*/, this /*OnConnectionFailedListener*/)
                .addApi(Auth.GOOGLE_SIGN_IN_API, gso)
                .build();
    }

    @Override
    protected void onStart(){
        super.onStart();

        OptionalPendingResult<GoogleSignInResult> opr = Auth.GoogleSignInApi.silentSignIn(mGoogleApiClient);
        if(opr.isDone()){
            GoogleSignInResult result = opr.get();
            GoogleSignInAccount account = result.getSignInAccount();
            Toast.makeText(LoginCheck.this, account.getId(), Toast.LENGTH_LONG).show();
            finish();
        }else if(AccessToken.getCurrentAccessToken() != null){
            Toast.makeText(LoginCheck.this, AccessToken.getCurrentAccessToken().getUserId().toString(), Toast.LENGTH_LONG).show();
            finish();
        }else{
            Toast.makeText(LoginCheck.this, "Need Sign in :)", Toast.LENGTH_LONG).show();
            Intent intent = new Intent(LoginCheck.this, LoginOverlayActivity.class);
            startActivity(intent);
        }
    }

    @Override
    public void onConnectionFailed(ConnectionResult connectionResult){
        Log.d("TAG", "onConnectionFailed : "+ connectionResult);
    }
}
