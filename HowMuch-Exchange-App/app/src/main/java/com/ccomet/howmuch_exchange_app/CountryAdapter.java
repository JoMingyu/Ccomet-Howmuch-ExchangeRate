package com.ccomet.howmuch_exchange_app;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by dsm2016 on 2017-05-18.
 */

public class CountryAdapter extends BaseAdapter {

    Context context;
    LayoutInflater inflater;
    ArrayList<String> countryList;
    int layout;

    public CountryAdapter(Context context, ArrayList<String> countryList, int layout) {
        this.context = context;
        this.inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        this.countryList = countryList;
        this.layout = layout;
    }

    @Override
    public int getCount() {
        return countryList.size();
    }

    @Override
    public Object getItem(int position) {
        return countryList.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if(convertView == null)
            convertView = inflater.inflate(layout, parent, false);

        TextView countryText = (TextView) convertView.findViewById(R.id.country);
        countryText.setText(countryList.get(position));

        return convertView;
    }
}
