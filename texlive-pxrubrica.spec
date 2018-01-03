Name:		texlive-pxrubrica
Version:	1.3b
Release:	1
Summary:	TeXLive pxrubrica package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxrubrica.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxrubrica.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxrubrica.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive pxrubrica package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/platex/pxrubrica
%doc %{_texmfdistdir}/doc/platex/pxrubrica
#- source
%doc %{_texmfdistdir}/source/platex/pxrubrica

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
