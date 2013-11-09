Summary:	Audio-to-audio and audio-to-midi alignment
Summary(pl.UTF-8):	Wyrównywanie dźwięku do dźwięku lub dźwięku do MIDI
Name:		scorealign
# version is svn rev of fetched source
Version:	227
Release:	1
License:	MIT-like
Group:		Applications/Sound
# svn co https://portmedia.svn.sourceforge.net/svnroot/portmedia/scorealign/trunk scorealign
Source0:	%{name}.tar.xz
# Source0-md5:	5d3eec56e4f45a915dfb6acfe115240e
Patch0:		%{name}-make.patch
Patch1:		%{name}-format.patch
Patch2:		%{name}-includes.patch
URL:		http://sourceforge.net/projects/portmedia/files/scorealign/
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	portsmf-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scorealign is a program for audio-to-audio and audio-to-midi
alignment.

%description -l pl.UTF-8
scorealign to program do wyrównywania dźwięku do dźwięku lub dźwięku
do MIDI.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} -f Makefile.linux \
	cc="%{__cc} %{rpmcflags} %{rpmcppflags} -DLINUX -Ifft3 -I/usr/include/portSMF" \
	c++="%{__cxx} %{rpmcxxflags} %{rpmcppflags} -DLINUX -Ifft3 -I/usr/include/portSMF" \
	c++link="%{__cxx} %{rpmcxxflags} %{rpmldflags}" \
	PORTSMF=/usr/include/portSMF \
	optimize="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D scorealign $RPM_BUILD_ROOT%{_bindir}/scorealign

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt changelog.txt license.txt 
%attr(755,root,root) %{_bindir}/scorealign
