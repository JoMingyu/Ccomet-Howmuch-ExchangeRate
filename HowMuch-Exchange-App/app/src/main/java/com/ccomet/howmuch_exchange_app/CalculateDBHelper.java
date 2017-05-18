package com.ccomet.howmuch_exchange_app;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import java.util.ArrayList;

/**
 * Created by dsm2016 on 2017-05-18.
 */

public class CalculateDBHelper extends SQLiteOpenHelper {
    String TABLENAME = "calculate_history";

    public CalculateDBHelper(Context context, String name, int version) {
        super(context, name, null, version);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE " + TABLENAME + "(" +
                "src_nation TEXT NOT NULL, " +
                "dst_nation TEXT NOT NULL, " +
                "exchange_rate REAL NOT NULL," +
                "calc_result REAL NOT NULL," +
                "timestamp DATETIME NOT NULL)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS" + TABLENAME);
        onCreate(db);
    }

    //DB에 레코드 저장
    public void insert(String src_nation, String dst_nation, Double exchange_rate, Double calc_result, String timestamp) {
        SQLiteDatabase db = getWritableDatabase();
        ContentValues values = new ContentValues();

        values.put("src_nation", src_nation);
        values.put("dst_nation", dst_nation);
        values.put("exchange_rate", exchange_rate);
        values.put("calc_result", calc_result);
        values.put("timestamp", timestamp);

        db.insert(TABLENAME, null, values);
        db.close();
    }

    public void delete(String timestamp) {
        SQLiteDatabase db = getWritableDatabase();
        db.execSQL("DELETE FROM " + TABLENAME+ "WHERE timestamp <= '"+timestamp+"'");
        db.close();
    }

    public ArrayList<CalculateInfo> getData() {
        SQLiteDatabase db = getReadableDatabase();
        ArrayList<CalculateInfo> dataList = new ArrayList<CalculateInfo>();

        Cursor cursor = db.rawQuery("SELECT * FROM " + TABLENAME, null);
        while(cursor.moveToNext()) {
            dataList.add(new CalculateInfo(

                    cursor.getString(0),
                    cursor.getString(1),
                    cursor.getDouble(2),
                    cursor.getDouble(3),
                    cursor.getString(4)
            ));
        }

        return dataList;
    }
}
