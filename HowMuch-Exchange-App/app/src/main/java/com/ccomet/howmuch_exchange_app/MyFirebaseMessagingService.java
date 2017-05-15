package com.ccomet.howmuch_exchange_app;

import android.widget.Toast;

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

/**
 * Created by 20311Leesoomin on 2017-04-05.
 */

public class MyFirebaseMessagingService extends FirebaseMessagingService {
    static final String TAG = MyFirebaseMessagingService.class.getName();

    @Override
    public void onMessageReceived(RemoteMessage remoteMessage){
        super.onMessageReceived(remoteMessage);

        if(remoteMessage.getData().size() > 0){
            String messageBody = remoteMessage.getData().get("message_body");
            if(messageBody != null){
                Toast.makeText(getApplicationContext(), messageBody, Toast.LENGTH_LONG);
            }
        }

        if(remoteMessage.getNotification() != null){
            final String messageBody = remoteMessage.getNotification().getBody();
            Toast.makeText(getApplicationContext(), messageBody, Toast.LENGTH_LONG);
        }
    }
}
