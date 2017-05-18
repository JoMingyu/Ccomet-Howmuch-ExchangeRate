package com.ccomet.howmuch_exchange_app;

import android.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;

/**
 * Created by dsm2016 on 2017-05-18.
 */

public class ExchangeListFragment extends Fragment {
    ListView exchangeList;
    ExchangeAdapter adapter;

    ArrayList<ExchangeInfo> datas;

    BookmarkDBHelper DBhleper;
    public ExchangeListFragment() {
    }

    public static ExchangeListFragment newInstance(ArrayList<ExchangeInfo> data) {
        ExchangeListFragment fragment = new ExchangeListFragment();
        Bundle args = new Bundle();
        args.putSerializable("exchangeList", data);
        fragment.setArguments(args);

        return fragment;
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.exchangelist_fragment, container, false);

        exchangeList = (ListView)view.findViewById(R.id.exchange_list);
        DBhleper = new BookmarkDBHelper(getActivity(), "Bookmark_DB.db", 1);

        datas = (ArrayList<ExchangeInfo>) getArguments().get("exchangeList");

        adapter = new ExchangeAdapter(getActivity(), datas, R.layout.exchange_view_layout);
        exchangeList.setAdapter(adapter);

        exchangeList.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
            @Override
            public boolean onItemLongClick(AdapterView<?> parent, View view, int position, long id){
                String src = datas.get(position).getSrc_nation();
                String dst = datas.get(position).getDst_nation();

                int flag = DBhleper.select(src, dst);
                //클릭한 아이템이 북마크일 때
                if(flag == 1) {
                    DBhleper.update(src, dst, 0);
                    Toast.makeText(getActivity(), "즐겨 찾기가 해제 되었습니다.", Toast.LENGTH_SHORT).show();
                } else if (flag == -1){
                    DBhleper.insert(src, dst);
                    Toast.makeText(getActivity(), "즐겨 찾기에 추가 되었습니다.", Toast.LENGTH_SHORT).show();
                } else {
                    DBhleper.update(src, dst, 1);
                    Toast.makeText(getActivity(), "즐겨 찾기로 설정 되었습니다.", Toast.LENGTH_SHORT).show();
                }

                return true;
            }
        });

        return view;
    }
}
