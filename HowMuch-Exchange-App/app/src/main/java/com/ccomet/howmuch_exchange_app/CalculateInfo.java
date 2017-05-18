package com.ccomet.howmuch_exchange_app;

/**
 * Created by dsm2016 on 2017-05-18.
 */
public class CalculateInfo {
    String src_nation;
    String dst_nation;
    String timestamp;
    Double exchange_rate;
    Double calc_result;

    public CalculateInfo(String src_nation, String dst_nation,  Double exchange_rate, Double calc_result, String timestamp) {
        this.src_nation = src_nation;
        this.dst_nation = dst_nation;
        this.timestamp = timestamp;
        this.exchange_rate = exchange_rate;
        this.calc_result = calc_result;
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

    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }

    public Double getExchange_rate() {
        return exchange_rate;
    }

    public void setExchange_rate(Double exchange_rate) {
        this.exchange_rate = exchange_rate;
    }

    public Double getCalc_result() {
        return calc_result;
    }

    public void setCalc_result(Double calc_result) {
        this.calc_result = calc_result;
    }
}
