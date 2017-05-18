package com.ccomet.howmuch_exchange_app;

import android.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.TextView;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.Locale;

/**
 * Created by dsm2016 on 2017-05-18.
 */

public class CalculatorFragment extends Fragment {
    Spinner src, dst;
    EditText rate;
    TextView result;
    Button button;

    ListView calcList;
    CalculateDBHelper dbHelper;
    CalculatorAdapter calcAdapter;

    ArrayList<CalculateInfo> calcData;
    ArrayList<ExchangeInfo> datas;
    ArrayList<String> countryList = new ArrayList<String>(Arrays.asList("ARS", "AUD", "BRL", "CAD", "CNY", "EUR", "GBP", "INR", "JPY", "KRW", "PHP", "SGD", "TRY", "USD"));

    public CalculatorFragment() {
    }

    public static CalculatorFragment newInstance(ArrayList<ExchangeInfo> data) {
        CalculatorFragment fragment = new CalculatorFragment();

        Bundle args = new Bundle();
        args.putSerializable("exchangeList", data);
        fragment.setArguments(args);

        return fragment;
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.calculator_fragment, container, false);

        datas = (ArrayList<ExchangeInfo>) getArguments().get("exchangeList");

        src = (Spinner) view.findViewById(R.id.calcSrc);
        dst = (Spinner) view.findViewById(R.id.calcDst);

        rate = (EditText) view.findViewById(R.id.calcRate);
        result = (TextView) view.findViewById(R.id.calcRes);
        button = (Button) view.findViewById(R.id.calcButton);

        ArrayAdapter<String> adapter = new ArrayAdapter<String>(getActivity(), android.R.layout.simple_spinner_item, countryList);
        src.setAdapter(adapter);
        dst.setAdapter(adapter);

        calcList = (ListView) view.findViewById(R.id.calcList);

        //버튼이 눌렸을 때 src, dst를 바탕으로 현율을 게산해줌
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String calcRes = null;

                int srcPosition = src.getSelectedItemPosition();
                int dstPosition = dst.getSelectedItemPosition();

                //src dst가 같은 데이터의 위치를 찾아 postion 으로 선언한 뒤 데이터를 참조하여 textview 세팅
                if(srcPosition != dstPosition) {
                    if(dstPosition < srcPosition){
                        dstPosition++;
                    }

                    int position = srcPosition * 13 + dstPosition-1;
                    String src_temp = datas.get(position).getSrc_nation();
                    String dst_temp = datas.get(position).getDst_nation();

                    //환율 정보 참조한뒤 입력값 * 환율 을 calcRes에 저장
                    Double exchange_rate = datas.get(position).getExchange_rate();
                    int inserted = Integer.valueOf(rate.getText().toString());

                    //결과값을 string형으로 바꾸고 계산결과를 DB에 저장
                    calcRes = Double.toString(exchange_rate * inserted);
                    insertToDB(src_temp, dst_temp, exchange_rate, exchange_rate * inserted);
                } else {
                    int inserted = Integer.valueOf(rate.getText().toString());

                    calcRes = Double.toString(inserted);
                }

                //결과값을 textview에 설정
                result.setText(calcRes);
            }
        });

        dbHelper = new CalculateDBHelper(getActivity(), "calculated_history.db", 1);
        calcData = dbHelper.getData();

        calcAdapter = new CalculatorAdapter(getActivity(), calcData, R.layout.calc_view_layout);
        calcList.setAdapter(calcAdapter);

        return view;
    }

    private void insertToDB(String srcNation, String dstNation, Double rate, Double calcRes) {
        //현재 시간을 가져오기
        SimpleDateFormat formatter = new SimpleDateFormat ( "yyyy.MM.dd HH:mm:ss", Locale.KOREA );
        Date currentTime = new Date ();
        String timestamp = formatter.format ( currentTime );

        dbHelper.insert(srcNation, dstNation, rate, calcRes, timestamp);
        calcAdapter.notifyDataSetChanged();
        calcList.setAdapter(calcAdapter);
    }
}