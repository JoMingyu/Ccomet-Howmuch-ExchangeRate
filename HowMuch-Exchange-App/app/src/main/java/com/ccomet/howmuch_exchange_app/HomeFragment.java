package com.ccomet.howmuch_exchange_app;

import android.app.Fragment;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.NumberPicker;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by dsm2016 on 2017-05-18.
 */

public class HomeFragment extends Fragment {

    BookmarkDBHelper dbHelper;
    ExchangeAdapter bookmarkAdapter;

    ListView bookmarkList;
    TextView srcToDstRateText;
    NumberPicker leftPicker, rightPicker;
    ImageButton refreshButton;

    String[] countryArray = new String[] {"AUD", "ARS", "BRL", "CAD", "CNY", "EUR", "GBP", "INR", "JPY", "KRW", "PHP", "SGD", "TRY", "USD"};
    ArrayList<ExchangeInfo> bookmarkData = new ArrayList<ExchangeInfo>();
    ArrayList<ExchangeInfo> exchangeData = new ArrayList<ExchangeInfo>();


    public HomeFragment() {
    }

    public static HomeFragment newInstance(ArrayList<ExchangeInfo> data) {

        Bundle args = new Bundle();

        HomeFragment fragment = new HomeFragment();
        args.putSerializable("exchangeList", data);
        fragment.setArguments(args);

        return fragment;
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.home_fragment, container, false);

        bookmarkList = (ListView)view.findViewById(R.id.bookmark_list);

        leftPicker = (NumberPicker) view.findViewById(R.id.left_country_picker);
        rightPicker = (NumberPicker) view.findViewById(R.id.right_country_picker);

        initPicker();

        exchangeData = (ArrayList<ExchangeInfo>) getArguments().get("exchangeList");

        dbHelper = new BookmarkDBHelper(getActivity(), "Bookmark_DB.db", 1);
        bookmarkData = getDataIndex(dbHelper.getData());

        bookmarkAdapter = new ExchangeAdapter(getActivity(), bookmarkData, R.layout.exchange_view_layout);
        bookmarkList.setAdapter(bookmarkAdapter);

        srcToDstRateText = (TextView) view.findViewById(R.id.srcToDstRate);

        refreshButton = (ImageButton) view.findViewById(R.id.refreshButton);
        refreshButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                int leftPosition = leftPicker.getValue();
                int rightPosition = rightPicker.getValue();

                if(leftPosition == rightPosition) {
                    srcToDstRateText.setText("1");
                } else {
                    if(rightPosition < leftPosition) {
                        rightPosition++;
                    }
                    int dataIndex = leftPosition * 13 + rightPosition -1;
                    String rate = Double.toString(exchangeData.get(dataIndex).getExchange_rate());

                    srcToDstRateText.setText(rate);
                }

            }
        });

        return view;
    }

    private void initPicker() {
        leftPicker.setMinValue(0);
        rightPicker.setMinValue(0);
        leftPicker.setMaxValue(countryArray.length-1);
        rightPicker.setMaxValue(countryArray.length-1);
        leftPicker.setDisplayedValues(countryArray);
        rightPicker.setDisplayedValues(countryArray);
        setDividerColor(leftPicker, R.color.backgroundcolor);
        setDividerColor(rightPicker, R.color.backgroundcolor);
    }

    private void setDividerColor(NumberPicker picker, int color) {
        java.lang.reflect.Field[] pickerFields = NumberPicker.class.getDeclaredFields();
        for(java.lang.reflect.Field pf : pickerFields) {
            if(pf.getName().equals("mSelectionDivider")) {
                pf.setAccessible(true);
                try {
                    ColorDrawable colorDrawable = new ColorDrawable(color);
                    pf.set(picker, colorDrawable);
                } catch(Exception e) {
                    e.printStackTrace();
                }
                break;
            }
        }
    }

    private ArrayList<ExchangeInfo> getDataIndex(ArrayList<String> stringData) {
        String[] array;
        int srcIndex, dstIndex;
        ArrayList<ExchangeInfo> dataList = new ArrayList<ExchangeInfo>();

        for(int i=0; i<stringData.size(); i++) {
            array = stringData.get(i).split(",");
            srcIndex = countryIndex(array[0]);
            dstIndex = countryIndex(array[1]);

            int dataIndex = srcIndex * 13 + dstIndex -1;
            dataList.add(exchangeData.get(dataIndex));
        }
        return dataList;
    }

    private int countryIndex(String countryCode) {
        int index = 0;

        switch(countryCode){
            case "AUD":
                index = 0;
                break;
            case "ARS":
                index = 1;
                break;
            case "BRL":
                index = 2;
                break;
            case "CAD":
                index = 3;
                break;
            case "CNY":
                index = 4;
                break;
            case "EUR":
                index = 5;
                break;
            case "GBP":
                index = 6;
                break;
            case "INR":
                index = 7;
                break;
            case "JPY":
                index = 8;
                break;
            case "KRW":
                index = 9;
                break;
            case "PHP":
                index = 10;
                break;
            case "SGD":
                index = 11;
                break;
            case "TRY":
                index = 12;
                break;
            case "USD":
                index = 13;
                break;
        }
        return index;
    }
}