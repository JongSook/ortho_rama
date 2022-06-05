% device = readmatrix('data for SPM.xlsx', 'Sheet', 'device', 'Range', 'B2:E101');
% our = readmatrix('data for SPM.xlsx', 'Sheet', 'our data', 'Range', 'B2:E101');
% device = readmatrix('data for SPM.xlsx', 'Sheet', 'device', 'Range', 'B2:C101');
% our = readmatrix('data for SPM.xlsx', 'Sheet', 'our data', 'Range', 'B2:C101');
% 
% D = device';
% O = our';

device_abad = (readmatrix('for spm.xlsx', 'Sheet', 'ref.from device', 'Range', 'B3:B103'))';
our_rt.abad = readmatrix('for spm.xlsx', 'Sheet', 'rt.abd-add', 'Range', 'B2:CX99');
our_lt.abad = readmatrix('for spm.xlsx', 'Sheet', 'lt. abd-add', 'Range', 'B2:CX99');

device_dfpf = (readmatrix('for spm.xlsx', 'Sheet', 'ref.from device', 'Range', 'C3:C103'))';
our_rt.dfpf = readmatrix('for spm.xlsx', 'Sheet', 'rt.df-pf', 'Range', 'B2:CX99');
our_lt.dfpf = readmatrix('for spm.xlsx', 'Sheet', 'lt.df-pf', 'Range', 'B2:CX99');

device_rotate = (readmatrix('for spm.xlsx', 'Sheet', 'ref.from device', 'Range', 'D3:D103'))';
our_rt.rotate = readmatrix('for spm.xlsx', 'Sheet', 'rt. rotation', 'Range', 'B2:CX99');
our_lt.rotate = readmatrix('for spm.xlsx', 'Sheet', 'Lt. rotation', 'Range', 'B2:CX99');

device_prog = (readmatrix('for spm.xlsx', 'Sheet', 'ref.from device', 'Range', 'E3:E103'))';
our_rt.prog = readmatrix('for spm.xlsx', 'Sheet', 'rt.progres', 'Range', 'B2:CX99');
our_lt.prog = readmatrix('for spm.xlsx', 'Sheet', 'lt.progres.', 'Range', 'B2:CX99');

muu = 0;
ct.abad = [device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;...
    device_abad;device_abad;device_abad;device_abad;device_abad;device_abad;device_abad];
ct.dfpf = [device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;...
    device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf;device_dfpf];
ct.rotate = [device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;...
    device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate;device_rotate];
ct.prog = [device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;...
    device_prog;device_prog;device_prog;device_prog;device_prog;device_prog;device_prog];

%%% ref.from device %%% abad #B %%% dfpf #C %%% rotate #D %%% prog #E %%%
%%% rt.abd-add %%% rt.df-pf %%% rt. rotation %%% rt.progres %%% B2:CX99 %%%
%%% lt.abd-add %%% lt.df-pf %%% Lt. rotation %%% lt.progres. %%% B2:CX99 %%%
%% One-sample t test

% spm = spm1d.stats.ttest_paired(our, device);
% spm = spm1d.stats.ttest(our - device);
% spm = spm1d.stats.ttest_paired(our, device);
% spmi = spm.inference(0.05, 'two_tailed', true)
% spmi.plot()

spmr1 = spm1d.stats.ttest(our_rt.abad - device_abad);
spml1 = spm1d.stats.ttest(our_lt.abad - device_abad);
spmr2 = spm1d.stats.ttest(our_rt.dfpf - device_dfpf);
spml2 = spm1d.stats.ttest(our_lt.dfpf - device_dfpf);
spmr3 = spm1d.stats.ttest(our_rt.rotate - device_rotate);
spml3 = spm1d.stats.ttest(our_lt.rotate - device_rotate);
spmr4 = spm1d.stats.ttest(our_rt.prog - device_prog);
spml4 = spm1d.stats.ttest(our_lt.prog - device_prog);

status = true;

figure('position', [100 600 1200 400])
% subplot(131)
% spm1d.plot.plot_meanSD(D, 'color','k');
% hold on
% spm1d.plot.plot_meanSD(OR, 'color','r');
% hold on
% spm1d.plot.plot_meanSD(OL, 'color','b');
% title('Mean and SD')

subplot(121)
spmir1 = spmr1.inference(0.05, 'two_tailed', status);
spmir1.plot();
spmir1.plot_threshold_label()
spmir1.plot_p_values()
title('Left (Inversion-Eversion)')
xlabel('Gait Cycle (%)')

subplot(122)
spmil1 = spml1.inference(0.05, 'two_tailed', status);
spmil1.plot();
spmil1.plot_threshold_label()
spmil1.plot_p_values()
title('Right (Inversion-Eversion)')
xlabel('Gait Cycle (%)')

figure('position', [300 400 1200 400])
subplot(121)
spmir2 = spmr2.inference(0.05, 'two_tailed', status);
spmir2.plot();
spmir2.plot_threshold_label()
spmir2.plot_p_values()
title('Left (Dorsiflexion-Plantar Flexion)')
xlabel('Gait Cycle (%)')

subplot(122)
spmil2 = spml2.inference(0.05, 'two_tailed', status);
spmil2.plot();
spmil2.plot_threshold_label()
spmil2.plot_p_values()
title('Right (Dorsiflexion-Plantar Flexion)')
xlabel('Gait Cycle (%)')

figure('position', [500 200 1200 400])
subplot(121)
spmir3 = spmr3.inference(0.05, 'two_tailed', status);
spmir3.plot();
spmir3.plot_threshold_label()
spmir3.plot_p_values()
title('Left (Foot Rotation)')
xlabel('Gait Cycle (%)')

subplot(122)
spmil3 = spml3.inference(0.05, 'two_tailed', status);
spmil3.plot();
spmil3.plot_threshold_label()
spmil3.plot_p_values()
title('Right (Foot Rotation)')
xlabel('Gait Cycle (%)')

figure('position', [700 000 1200 400])
subplot(121)
spmir4 = spmr4.inference(0.05, 'two_tailed', status);
spmir4.plot();
spmir4.plot_threshold_label()
spmir4.plot_p_values()
title('Left (Foot Progression)')
xlabel('Gait Cycle (%)')

subplot(122)
spmil4 = spml4.inference(0.05, 'two_tailed', status);
spmil4.plot();
spmil4.plot_threshold_label()
spmil4.plot_p_values()
title('Right (Foot Progression)')
xlabel('Gait Cycle (%)')
%% Paired t test

spmr1 = spm1d.stats.ttest_paired(our_rt.abad, our_lt.abad);
spml1 = spm1d.stats.ttest_paired(our_lt.abad, our_rt.abad);
spmr2 = spm1d.stats.ttest_paired(our_rt.dfpf, our_lt.dfpf);
spml2 = spm1d.stats.ttest_paired(our_lt.dfpf, our_rt.dfpf);
spmr3 = spm1d.stats.ttest_paired(our_rt.rotate, our_lt.rotate);
spml3 = spm1d.stats.ttest_paired(our_lt.rotate, our_rt.rotate);
spmr4 = spm1d.stats.ttest_paired(our_rt.prog, our_lt.prog);
spml4 = spm1d.stats.ttest_paired(our_lt.prog, our_rt.prog);

status = true;

figure('position', [100 150 1200 800])

subplot(221)
spmir1 = spmr1.inference(0.05, 'two_tailed', status);
spmir1.plot();
spmir1.plot_threshold_label()
spmir1.plot_p_values()
title('Inversion-Eversion')
xlabel('Gait Cycle (%)')

subplot(222)
spmir1 = spmr2.inference(0.05, 'two_tailed', status);
spmir1.plot();
spmir1.plot_threshold_label()
spmir1.plot_p_values()
title('Dorsiflexion-Plantar Flexion')
xlabel('Gait Cycle (%)')

subplot(223)
spmir1 = spmr3.inference(0.05, 'two_tailed', status);
spmir1.plot();
spmir1.plot_threshold_label()
spmir1.plot_p_values()
title('Foot Rotation')
xlabel('Gait Cycle (%)')

subplot(224)
spmir1 = spmr4.inference(0.05, 'two_tailed', status);
spmir1.plot();
spmir1.plot_threshold_label()
spmir1.plot_p_values()
title('Foot Progression')
xlabel('Gait Cycle (%)')
%% Mean SD

% (Mean and SD)

figure('position', [0 0 1500 1000])

subplot(221)
b1 = spm1d.plot.plot_meanSD(device_abad, 'color','k');
hold on
b2 = spm1d.plot.plot_meanSD(our_rt.abad, 'color','r');
title('Inversion-Eversion (Mean and SD)')
xlabel('Gait Cycle (%)')
ylabel('Kinematic Angle (°)')
legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')

subplot(222)
b1 = spm1d.plot.plot_meanSD(device_dfpf, 'color','k');
hold on
b2 = spm1d.plot.plot_meanSD(our_rt.dfpf, 'color','r');
title('Dorsiflexion-Plantar Flexion (Mean and SD)')
xlabel('Gait Cycle (%)')
ylabel('Kinematic Angle (°)')
legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')

subplot(223)
b1 = spm1d.plot.plot_meanSD(device_rotate, 'color','k');
hold on
b2 = spm1d.plot.plot_meanSD(our_lt.rotate, 'color','r');
title('Foot Rotation (Mean and SD)')
xlabel('Gait Cycle (%)')
ylabel('Kinematic Angle (°)')
legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')

subplot(224)
b1 = spm1d.plot.plot_meanSD(device_prog, 'color','k');
hold on
b2 = spm1d.plot.plot_meanSD(our_rt.prog, 'color','r');
title('Foot Progression (Mean and SD)')
xlabel('Gait Cycle (%)')
ylabel('Kinematic Angle (°)')
legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')

% figure('position', [0 100 600 400])
% b1 = spm1d.plot.plot_meanSD(device_abad, 'color','k');
% hold on
% b2 = spm1d.plot.plot_meanSD(our_lt.abad, 'color','r');
% title('Inversion-Eversion')
% xlabel('Gait Cycle (%)')
% ylabel('Kinematic Angle (°)')
% legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')
% 
% figure('position', [100 150 600 400])
% b1 = spm1d.plot.plot_meanSD(device_dfpf, 'color','k');
% hold on
% b2 = spm1d.plot.plot_meanSD(our_lt.dfpf, 'color','r');
% title('Dorsiflexion-Plantar Flexion')
% xlabel('Gait Cycle (%)')
% ylabel('Kinematic Angle (°)')
% legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')
% 
% figure('position', [200 200 600 400])
% b1 = spm1d.plot.plot_meanSD(device_rotate, 'color','k');
% hold on
% b2 = spm1d.plot.plot_meanSD(our_lt.rotate, 'color','r');
% title('Foot Rotation')
% xlabel('Gait Cycle (%)')
% ylabel('Kinematic Angle (°)')
% legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')
% 
% figure('position', [300 250 600 400])
% b1 = spm1d.plot.plot_meanSD(device_prog, 'color','k');
% hold on
% b2 = spm1d.plot.plot_meanSD(our_lt.prog, 'color','r');
% title('Foot Progression')
% xlabel('Gait Cycle (%)')
% ylabel('Kinematic Angle (°)')
% legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')
% 
% figure('position', [400 300 600 400])
% b1 = spm1d.plot.plot_meanSD(device_abad, 'color','k');
% hold on
% b2 = spm1d.plot.plot_meanSD(our_rt.abad, 'color','r');
% title('Inversion-Eversion')
% xlabel('Gait Cycle (%)')
% ylabel('Kinematic Angle (°)')
% legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')
% 
% figure('position', [500 350 600 400])
% b1 = spm1d.plot.plot_meanSD(device_dfpf, 'color','k');
% hold on
% b2 = spm1d.plot.plot_meanSD(our_rt.dfpf, 'color','r');
% title('Dorsiflexion-Plantar Flexion')
% xlabel('Gait Cycle (%)')
% ylabel('Kinematic Angle (°)')
% legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')
% 
% figure('position', [600 100 600 400])
% b1 = spm1d.plot.plot_meanSD(device_rotate, 'color','k');
% hold on
% b2 = spm1d.plot.plot_meanSD(our_lt.rotate, 'color','r');
% title('Foot Rotation')
% xlabel('Gait Cycle (%)')
% ylabel('Kinematic Angle (°)')
% legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')
% 
% figure('position', [700 150 600 400])
% b1 = spm1d.plot.plot_meanSD(device_prog, 'color','k');
% hold on
% b2 = spm1d.plot.plot_meanSD(our_rt.prog, 'color','r');
% title('Foot Progression')
% xlabel('Gait Cycle (%)')
% ylabel('Kinematic Angle (°)')
% legend([b1 b2],{'Motion Program','Thai Healthy'},'Location','northeast')