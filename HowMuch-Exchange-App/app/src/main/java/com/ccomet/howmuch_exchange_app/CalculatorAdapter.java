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

public class CalculatorAdapter extends BaseAdapter {
    Context context;
    LayoutInflater inflater;
    ArrayList<CalculateInfo> calcList;
    int layout;

    public CalculatorAdapter(Context context, ArrayList<CalculateInfo> calcList, int layout) {
        this.context = context;
        this.inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        this.calcList = calcList;
        this.layout = layout;
    }

    @Override
    public int getCount() {
        return calcList.size();
    }

    @Override
    public Object getItem(int position) {
        return calcList.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if(convertView == null)
            convertView = inflater.inflate(layout, parent, false);

        TextView country = (TextView) convertView.findViewById(R.id.calcHistoryCountry);
        TextView rate = (TextView) convertView.findViewById(R.id.calcHistoryRate);
        TextView timestamp = (TextView) convertView.findViewById(R.id.calcHistoryTime);

        country.setText(calcList.get(position).getSrc_nation() + "->" + calcList.get(position).getDst_nation());
        rate.setText(calcList.get(position).getCalc_result().toString());
        timestamp.setText(calcList.get(position).getTimestamp());

        return convertView;
    }
}
