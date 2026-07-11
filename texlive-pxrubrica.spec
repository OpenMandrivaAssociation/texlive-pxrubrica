%global tl_name pxrubrica
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3e
Release:	%{tl_revision}.1
Summary:	Ruby annotations according to JIS X 4051
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/latex/pxrubrica
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxrubrica.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxrubrica.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pxrubrica.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a function to add ruby annotations (furigana) that
follow the style conventional in Japanese typography as described in the
W3C technical note "Requirements for Japanese Text Layout" ([JLREQ]) and
the JIS specification JIS X 4051. Starting with version 1.3, this
package also provides a function to add kenten (emphasis marks) to
Japanese text.

