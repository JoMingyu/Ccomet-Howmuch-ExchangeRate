package com.ccomet.howmuch_exchange_app;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.CursorIndexOutOfBoundsException;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import java.util.ArrayList;

/**
 * Created by dsm2016 on 2017-05-18.
 */

public class BookmarkDBHelper extends SQLiteOpenHelper {
    String TABLENAME = "bookmark";

    public BookmarkDBHelper(Context context, String name, int version) {
        super(context, name, null, version);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL("CREATE TABLE " + TABLENAME + "(" +
                "src_nation TEXT NOT NULL, " +
                "dst_nation TEXT NOT NULL," +
                "is_marked INTEGER DEFAULT 0," +
                "PRIMARY KEY(src_nation, dst_nation))");
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS "+ TABLENAME);
        onCreate(db);
    }

    public void insert(String src_nation, String dst_nation) {
        SQLiteDatabase db = getWritableDatabase();
        ContentValues values = new ContentValues();

        values.put("src_nation", src_nation);
        values.put("dst_nation", dst_nation);
        values.put("is_marked", 1);

        db.insert(TABLENAME, null, values);

        db.close();
    }

    public void delete(String src_nation, String dst_nation) {
        SQLiteDatabase db = getWritableDatabase();

        db.execSQL("DELETE FROM "+ TABLENAME +" WHERE " +
                "src_nation='"+ src_nation +"' AND dst_nation='"+ dst_nation +"'");
        db.close();
    }

    public void update(String src_nation, String dst_nation, int isMarked) {
        SQLiteDatabase db = getWritableDatabase();

        String query = "UPDATE "+TABLENAME+" SET is_marked="+ isMarked+
                " WHERE src_nation='"+src_nation+"' AND dst_nation='"+dst_nation+"'";
        db.execSQL(query);
    }

    public int select(String src_nation, String dst_nation) {
        SQLiteDatabase db = getReadableDatabase();

        Cursor cursor = db.rawQuery("SELECT is_marked FROM " + TABLENAME + " WHERE src_nation=? AND dst_nation=?", new String[] {src_nation, dst_nation});
        try {
            if(cursor.getInt(0) == 0) {
                return -1;
            }
        } catch (CursorIndexOutOfBoundsException e) {
            e.printStackTrace();
            return 0;
        }

        int count = cursor.getCount();
        cursor.close();

        return count;
    }


    public ArrayList<String> getData() {
        SQLiteDatabase db = getReadableDatabase();
        ArrayList<String> dataList = new ArrayList<String>();

        Cursor cursor = db.rawQuery("SELECT src_nation, dst_nation FROM " + TABLENAME + " WHERE is_marked=1", null);
        while(cursor.moveToNext()){
            dataList.add(cursor.getString(0) + "," + cursor.getString(1));
        }

        return dataList;
    }
}
