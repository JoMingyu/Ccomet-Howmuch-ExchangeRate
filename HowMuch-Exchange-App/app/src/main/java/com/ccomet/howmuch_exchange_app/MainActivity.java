package com.ccomet.howmuch_exchange_app;

import android.*;
import android.Manifest;
import android.content.DialogInterface;
import android.content.pm.PackageManager;
import android.os.Build;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    TextView permissionText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        permissionText = (TextView)findViewById(R.id.permission_text);
    }

    @Override
    protected void onResume(){
        super.onResume();

        //get Permissions
        if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.M){
            int permissionResult = checkSelfPermission(Manifest.permission.READ_PHONE_STATE);
            if(permissionResult == PackageManager.PERMISSION_DENIED){
                //If application doesn't have permission
                if(shouldShowRequestPermissionRationale(Manifest.permission.READ_PHONE_STATE)){
                    AlertDialog.Builder dialog = new AlertDialog.Builder(MainActivity.this);
                    dialog.setTitle("Need Permission")
                            .setMessage("This application needs to READ_PHONE_STATE Permission. Continue?")
                            .setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                                @Override
                                public void onClick(DialogInterface dialog, int which) {
                                    if(Build.VERSION.SDK_INT >= Build.VERSION_CODES.M){
                                        requestPermissions(new String[]{Manifest.permission.READ_PHONE_STATE}, 1000);
                                    }
                                }
                            })
                            .setNegativeButton("No", new DialogInterface.OnClickListener() {
                                @Override
                                public void onClick(DialogInterface dialog, int which) {
                                    Toast.makeText(MainActivity.this, "Canceled", Toast.LENGTH_LONG).show();
                                }
                            })
                            .create()
                            .show();
                }else{
                    requestPermissions(new String[]{Manifest.permission.READ_PHONE_STATE}, 1000);
                }
            }else{
                permissionText.setText("Permission : GRANTED");
            }
        }else{
            permissionText.setText("Permission : GRANTED");
        }
    }
}
