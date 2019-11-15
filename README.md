# Bidirectional Conditional Insertion Sort (BCIS)

This is an attempt to reproduce an alternative to classic insertion sort algorithm, proposed originally in the article *Bidirectional conditional insertion sort algorithm: An efficient progress on the classical insertion sort.*

### How Does It Work

- **data_generator.py**: creates normal, poisson, binominal and uniform distributions which will be used in algorithm tests.
- **main.py**: runs performance tests using distributions generated
- **real_data.csv**: a set of real crime data obtained from [Spatial Data](https://support.spatialkey.com/spatialkey-sample-csv-data/) site
- **distributions.csv**: file generate by **data_generator.py**
- **ratios.csv**:  report generated after ran **main.py**
### References

Mohammed, A. S., Amrahov, Ş. E., & Çelebi, F. V. (2017). Bidirectional conditional insertion sort algorithm: An efficient progress on the classical insertion sort. *Future Generation Computer Systems*, 71, 102-112.