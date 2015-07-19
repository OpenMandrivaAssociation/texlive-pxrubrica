# revision 28494
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-pxrubrica
Version:	20131010
Release:	9
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
%{_texmfdistdir}/tex/platex/pxrubrica/pxrubrica.sty
%doc %{_texmfdistdir}/doc/platex/pxrubrica/LICENSE
%doc %{_texmfdistdir}/doc/platex/pxrubrica/README
%doc %{_texmfdistdir}/doc/platex/pxrubrica/pxrubrica-en.pdf
%doc %{_texmfdistdir}/doc/platex/pxrubrica/pxrubrica-en.tex
%doc %{_texmfdistdir}/doc/platex/pxrubrica/pxrubrica.pdf
%doc %{_texmfdistdir}/doc/platex/pxrubrica/sample/test-jlreq.pdf
%doc %{_texmfdistdir}/doc/platex/pxrubrica/sample/test-jlreq.tex
%doc %{_texmfdistdir}/doc/platex/pxrubrica/sample/test-sf.pdf
%doc %{_texmfdistdir}/doc/platex/pxrubrica/sample/test-sf.tex
%doc %{_texmfdistdir}/doc/platex/pxrubrica/sample/test-toc.pdf
%doc %{_texmfdistdir}/doc/platex/pxrubrica/sample/test-toc.tex
#- source
%doc %{_texmfdistdir}/source/platex/pxrubrica/pxrubrica.dtx
%doc %{_texmfdistdir}/source/platex/pxrubrica/pxrubrica.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
