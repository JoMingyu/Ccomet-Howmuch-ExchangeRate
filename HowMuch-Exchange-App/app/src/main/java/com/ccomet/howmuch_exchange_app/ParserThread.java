package com.ccomet.howmuch_exchange_app;

import android.os.AsyncTask;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

/**
 * Created by dsm2016 on 2017-05-18.
 */

public class ParserThread extends AsyncTask<String, Void, ArrayList<ExchangeInfo>> {
    @Override
    protected ArrayList<ExchangeInfo> doInBackground(String... params) {
        try {
            String addUrl = "";
            //1번째 인가값은 원래 52.79.134.200:81/exchange 2번째는 src_nation, 3번쨰는 dst_nation
            if(params.length != 1) {
                addUrl = '?' + "src_nation=" + params[1] + '&' + "dst_nation=" + params[2];
            }

            URL url = new URL(params[0] + addUrl);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();

            //GET방식으로 리퀘스트 요청
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setDoInput(true); conn.setDoOutput(false);

            StringBuilder builder = new StringBuilder();
            int responseCode = conn.getResponseCode();
            String string;

            if(responseCode == HttpURLConnection.HTTP_OK) {
                BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));

                while((string = reader.readLine()) != null) {
                    builder.append(string + '\n');
                }
                reader.close();
                JSONArray array = new JSONArray(builder.toString());
                return refineArray(array);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    private ArrayList<ExchangeInfo> refineArray(JSONArray array) {
        ArrayList<ExchangeInfo> datas = new ArrayList<ExchangeInfo>();
        String src, dst;
        Double rate;

        try {
            for(int i=0; i<array.length(); i++) {
                JSONObject json = array.getJSONObject(i);

                src = (String) json.get("src_nation");
                dst = (String) json.get("dst_nation");
                rate = (Double) json.get("exchange_rate");

                datas.add(new ExchangeInfo(src, dst, rate));
            }
            return datas;

        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}
