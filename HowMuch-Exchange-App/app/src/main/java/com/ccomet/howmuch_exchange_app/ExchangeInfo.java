package com.ccomet.howmuch_exchange_app;

/**
 * Created by dsm2016 on 2017-05-18.
 */


public class ExchangeInfo
{
    private String src_nation;
    private String dst_nation;
    private double exchange_rate;

    public ExchangeInfo(String src_nation, String dst_nation, double exchange_rate)
    {
        this.src_nation = src_nation;
        this.dst_nation = dst_nation;
        this.exchange_rate = exchange_rate;
    }

    public String getSrc_nation() {
        return src_nation;
    }

    public void setSrc_nation(String src_nation) {
        this.src_nation = src_nation;
    }

    public String getDst_nation() {
        return dst_nation;
    }

    public void setDst_nation(String dst_nation) {
        this.dst_nation = dst_nation;
    }

    public double getExchange_rate() {
        return exchange_rate;
    }

    public void setExchange_rate(double exchange_rate) {
        this.exchange_rate = exchange_rate;
    }

}