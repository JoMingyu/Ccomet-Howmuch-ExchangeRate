package com.ccomet.howmuch_exchange_app;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by dsm2016 on 2017-05-18.
 */

public class ExchangeAdapter extends BaseAdapter
{
    Context context;
    LayoutInflater inflater;
    ArrayList<ExchangeInfo> exchangeList;
    int layout;


    public ExchangeAdapter(Context context, ArrayList<ExchangeInfo> exchangeList, int layout) {
        this.context = context;
        this.inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
        this.exchangeList = exchangeList;
        this.layout = layout;
    }

    @Override
    public int getCount() {
        return exchangeList.size();
    }

    @Override
    public Object getItem(int position) {
        return exchangeList.get(position).getExchange_rate();
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(final int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = inflater.inflate(layout, parent, false);
        }

        BookmarkDBHelper helper = new BookmarkDBHelper(context, "Bookmark_DB.db", 1);

        TextView exchange_country_text = (TextView) convertView.findViewById(R.id.exchange_country);
        TextView exchange_rate_text = (TextView) convertView.findViewById(R.id.exchange_rate);
        ImageView isBookmark = (ImageView) convertView.findViewById(R.id.bookmark_img);

        final String exchange_country = exchangeList.get(position).getSrc_nation() + " -> " + exchangeList.get(position).getDst_nation();
        String exchange_rate = Double.toString(exchangeList.get(position).getExchange_rate());
        int isMarked= helper.select(exchangeList.get(position).getSrc_nation(), exchangeList.get(position).getDst_nation());

        exchange_country_text.setText(exchange_country);
        exchange_rate_text.setText(exchange_rate);

        if(isMarked == 1) {
            isBookmark.setImageResource(R.drawable.star);
        } else {
            isBookmark.setImageResource(R.drawable.emptystar);
        }

        return convertView;
    }
}