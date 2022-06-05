%% get .xlsx data file

filename = 'for spm.xlsx';
status_ttest = true;
status_ttest_paired = true;

device.abad = readmatrix(filename, 'Sheet', 'ref.from device', 'Range', 'B3:B103')';
our_rt.abad = readmatrix(filename, 'Sheet', 'rt.abd-add', 'Range', 'B2:CX99');
our_lt.abad = readmatrix(filename, 'Sheet', 'lt. abd-add', 'Range', 'B2:CX99');

device.dfpf = readmatrix(filename, 'Sheet', 'ref.from device', 'Range', 'C3:C103')';
our_rt.dfpf = readmatrix(filename, 'Sheet', 'rt.df-pf', 'Range', 'B2:CX99');
our_lt.dfpf = readmatrix(filename, 'Sheet', 'lt.df-pf', 'Range', 'B2:CX99');

device.rotate = readmatrix(filename, 'Sheet', 'ref.from device', 'Range', 'D3:D103')';
our_rt.rotate = readmatrix(filename, 'Sheet', 'rt. rotation', 'Range', 'B2:CX99');
our_lt.rotate = readmatrix(filename, 'Sheet', 'Lt. rotation', 'Range', 'B2:CX99');

device.prog = readmatrix(filename, 'Sheet', 'ref.from device', 'Range', 'E3:E103')';
our_rt.prog = readmatrix(filename, 'Sheet', 'rt.progres', 'Range', 'B2:CX99');
our_lt.prog = readmatrix(filename, 'Sheet', 'lt.progres.', 'Range', 'B2:CX99');

muu = 0;

%%% ref.from device %%% abad #B %%% dfpf #C %%% rotate #D %%% prog #E %%%
%%% rt.abd-add %%% rt.df-pf %%% rt. rotation %%% rt.progres %%% B2:CX99 %%%
%%% lt.abd-add %%% lt.df-pf %%% Lt. rotation %%% lt.progres. %%% B2:CX99 %%%
%% One-sample t test

% spm = spm1d.stats.ttest_paired(our, device);
% spm = spm1d.stats.ttest(our - device);
% spm = spm1d.stats.ttest_paired(our, device);
% spmi = spm.inference(0.05, 'two_tailed', true)
% spmi.plot()

spmr1 = spm1d.stats.ttest(our_rt.abad - device.abad);
spml1 = spm1d.stats.ttest(our_lt.abad - device.abad);
spmr2 = spm1d.stats.ttest(our_rt.dfpf - device.dfpf);
spml2 = spm1d.stats.ttest(our_lt.dfpf - device.dfpf);
spmr3 = spm1d.stats.ttest(our_rt.rotate - device.rotate);
spml3 = spm1d.stats.ttest(our_lt.rotate - device.rotate);
spmr4 = spm1d.stats.ttest(our_rt.prog - device.prog);
spml4 = spm1d.stats.ttest(our_lt.prog - device.prog);

figure('position', [100 600 1200 400]);

subplot(121);
spmir1 = spmr1.inference(0.05, 'two_tailed', status_ttest);
spmir1.plot();
spmir1.plot_threshold_label();
spmir1.plot_p_values();
title('Left (Inversion-Eversion)');
xlabel('Gait Cycle (%)');

subplot(122);
spmil1 = spml1.inference(0.05, 'two_tailed', status_ttest);
spmil1.plot();
spmil1.plot_threshold_label();
spmil1.plot_p_values();
title('Right (Inversion-Eversion)');
xlabel('Gait Cycle (%)');

figure('position', [300 400 1200 400]);
subplot(121);
spmir2 = spmr2.inference(0.05, 'two_tailed', status_ttest);
spmir2.plot();
spmir2.plot_threshold_label();
spmir2.plot_p_values();
title('Left (Dorsiflexion-Plantar Flexion)');
xlabel('Gait Cycle (%)');

subplot(122);
spmil2 = spml2.inference(0.05, 'two_tailed', status_ttest);
spmil2.plot();
spmil2.plot_threshold_label();
spmil2.plot_p_values();
title('Right (Dorsiflexion-Plantar Flexion)');
xlabel('Gait Cycle (%)');

figure('position', [500 200 1200 400]);
subplot(121);
spmir3 = spmr3.inference(0.05, 'two_tailed', status_ttest);
spmir3.plot();
spmir3.plot_threshold_label();
spmir3.plot_p_values();
title('Left (Foot Rotation)');
xlabel('Gait Cycle (%)');

subplot(122);
spmil3 = spml3.inference(0.05, 'two_tailed', status_ttest);
spmil3.plot();
spmil3.plot_threshold_label();
spmil3.plot_p_values();
title('Right (Foot Rotation)');
xlabel('Gait Cycle (%)');

figure('position', [700 000 1200 400]);
subplot(121);
spmir4 = spmr4.inference(0.05, 'two_tailed', status_ttest);
spmir4.plot();
spmir4.plot_threshold_label();
spmir4.plot_p_values();
title('Left (Foot Progression)');
xlabel('Gait Cycle (%)');

subplot(122);
spmil4 = spml4.inference(0.05, 'two_tailed', status_ttest);
spmil4.plot();
spmil4.plot_threshold_label();
spmil4.plot_p_values();
title('Right (Foot Progression)');
xlabel('Gait Cycle (%)');
%% Paired t test

spmr1 = spm1d.stats.ttest_paired(our_rt.abad, our_lt.abad);
spml1 = spm1d.stats.ttest_paired(our_lt.abad, our_rt.abad);
spmr2 = spm1d.stats.ttest_paired(our_rt.dfpf, our_lt.dfpf);
spml2 = spm1d.stats.ttest_paired(our_lt.dfpf, our_rt.dfpf);
spmr3 = spm1d.stats.ttest_paired(our_rt.rotate, our_lt.rotate);
spml3 = spm1d.stats.ttest_paired(our_lt.rotate, our_rt.rotate);
spmr4 = spm1d.stats.ttest_paired(our_rt.prog, our_lt.prog);
spml4 = spm1d.stats.ttest_paired(our_lt.prog, our_rt.prog);

figure('position', [100 150 1200 800]);

subplot(221);
spmir1 = spmr1.inference(0.05, 'two_tailed', status_ttest_paired);
spmir1.plot();
spmir1.plot_threshold_label();
spmir1.plot_p_values();
title('Inversion-Eversion');
xlabel('Gait Cycle (%)');

subplot(222);
spmir1 = spmr2.inference(0.05, 'two_tailed', status_ttest_paired);
spmir1.plot();
spmir1.plot_threshold_label();
spmir1.plot_p_values();
title('Dorsiflexion-Plantar Flexion');
xlabel('Gait Cycle (%)');

subplot(223);
spmir1 = spmr3.inference(0.05, 'two_tailed', status_ttest_paired);
spmir1.plot();
spmir1.plot_threshold_label();
spmir1.plot_p_values();
title('Foot Rotation');
xlabel('Gait Cycle (%)');

subplot(224);
spmir1 = spmr4.inference(0.05, 'two_tailed', status_ttest_paired);
spmir1.plot();
spmir1.plot_threshold_label();
spmir1.plot_p_values();
title('Foot Progression');
xlabel('Gait Cycle (%)');
%% Mean SD

figure('position', [0 0 1500 1000]);

subplot(221);
b1 = spm1d.plot.plot_meanSD(device.abad, 'color','k');
hold on;
b2 = spm1d.plot.plot_meanSD(our_rt.abad, 'color','r');
title('Inversion-Eversion (Mean and SD)');
xlabel('Gait Cycle (%)');
ylabel('Kinematic Angle (°)');
legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast');

subplot(222);
b1 = spm1d.plot.plot_meanSD(device.dfpf, 'color','k');
hold on;
b2 = spm1d.plot.plot_meanSD(our_rt.dfpf, 'color','r');
title('Dorsiflexion-Plantar Flexion (Mean and SD)');
xlabel('Gait Cycle (%)');
ylabel('Kinematic Angle (°)');
legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast');

subplot(223);
b1 = spm1d.plot.plot_meanSD(device.rotate, 'color','k');
hold on;
b2 = spm1d.plot.plot_meanSD(our_lt.rotate, 'color','r');
title('Foot Rotation (Mean and SD)');
xlabel('Gait Cycle (%)');
ylabel('Kinematic Angle (°)');
legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast');

subplot(224);
b1 = spm1d.plot.plot_meanSD(device.prog, 'color','k');
hold on;
b2 = spm1d.plot.plot_meanSD(our_rt.prog, 'color','r');
title('Foot Progression (Mean and SD)');
xlabel('Gait Cycle (%)');
ylabel('Kinematic Angle (°)');
legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast');