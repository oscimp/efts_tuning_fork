x=load('measurement.txt');
[~,fr]=max(x(:,3));fr=x(fr,1);
[FitResultsm,GOF,baseline,coeff,residual,xm,ym]=peakfit([x(:,1) x(:,4).^2],fr,0,1,2,0,100,[fr 310000],0,0,0)
                                                      % signal,center,window,NumPeaks,peakshape
[FitResultse,GOF,baseline,coeff,residual,xe,ye]=peakfit([x(:,1) x(:,5).^2],fr,0,1,2,0,100,[fr 310000],0,0,0)
close all
subplot(211)
errorbar(x(:,1),x(:,2),0.02)
hold on
errorbar(x(:,1),x(:,4),0.02)
plot(xm,sqrt(ym))
xlabel('frequency (Hz)')
ylabel('displacement (pixel)')
legend('drive=0.7','drive=0.2','fit')
subplot(212)
errorbar(x(:,1),x(:,3),20)
hold on
errorbar(x(:,1),x(:,5),20)
plot(xe,sqrt(ye))
xlabel('frequency (Hz)')
ylabel('amplitude (V)')
legend('drive=0.7','drive=0.2','fit')

k=find(x(:,5)>max(x(:,5)/2));Qele=fr/(x(k(end),1)-x(k(1),1))
k=find(x(:,4)>max(x(:,4)/2));Qmec=fr/(x(k(end),1)-x(k(1),1))
                                  fr/(x(k(end),1)-x(k(1)+1,1)) % for error bar


FitResultse 
%   1.0000e+00   3.2760e+04   3.1176e+05   3.3490e+00   1.2993e+06

%   1.0000e+00   3.2760e+04   6.4216e+02   3.3928e+00   2.7019e+03
%
FitResultsm
%   1.0000e+00   3.2760e+04   1.1739e+00   3.3576e+00   4.9019e+00
