%% 
n=(1:50)*2*pi;
for t = 1:1000
    Y = sin(n*50/t);
   plot(Y);     %plot shows a sine wave with decreasing frequency

   F(t) = getframe; %I capture the plot here


end

writerObj = VideoWriter('test2.avi'); %Attempt to create an avi
open(writerObj);
for t= 1:time

    writeVideo(writerObj,F(t))

end

close(writerObj);
%% 
time = 100;
for t = 1:time
   fplot(@(x) sin(x*50/t),[0,2*pi]);  % plot
   ylim([-1,1]);                      % guarantee consistent height
   F(t) = getframe;                   % capture it
end

writerObj = VideoWriter('test2.avi');
open(writerObj);
writeVideo(writerObj, F(t))
close(writerObj);
%% 
n=(1:50)*2*pi ;

Y = sin(n*50) ;
hp = plot(Y) ;              %// Generate the initial plot (and retrieve the handle of the graphic object)
ylim([-1,1]) ;              %// Set the Y axes limits (once and for all)

writerObj = VideoWriter('test2.avi'); %// initialize the VideoWriter object
open(writerObj) ;
for t = 1:1000
   Y = sin(n*50/t) ;        %// calculate new Y values
   set(hp,'YData',Y) ;      %// update the plot data (this does not generate a "new" plot), nor resize the axes

%    fplot(@(x) sin(x*50/t),[0,2*pi]);  % plot
%    ylim([-1,1]);                      % guarantee consistent height
   
   F(t) = getframe ;           %// Capture the frame
   writeVideo(writerObj,F(t))  %// add the frame to the movie
end
close(writerObj);