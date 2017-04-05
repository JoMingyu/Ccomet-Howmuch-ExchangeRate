package com.ccomet.howmuch_exchange_app;

import android.util.Log;

/**
 * Created by 20311Leesoomin on 2017-04-05.
 */

public class FirebaseInstanceId extends com.google.firebase.iid.FirebaseInstanceIdService{
    private static final String TAG = "MainScreen";

    @Override
    public void onTokenRefresh(){
        String token = com.google.firebase.iid.FirebaseInstanceId.getInstance().getToken();
        Log.d(TAG, token);
    }
}
