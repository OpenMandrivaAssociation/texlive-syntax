Name:		texlive-syntax
Version:	15878
Release:	2
Summary:	Creation of syntax diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/syntax
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntax.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntax.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Create syntax diagrams using special environments and commands
to represent the diagram structure.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/syntax/syntax.tex
%doc %{_texmfdistdir}/doc/latex/syntax/README
%doc %{_texmfdistdir}/doc/latex/syntax/syntaxintro.pdf
%doc %{_texmfdistdir}/doc/latex/syntax/syntaxintro.tex
%doc %{_texmfdistdir}/doc/latex/syntax/syntaxtest.pdf
%doc %{_texmfdistdir}/doc/latex/syntax/syntaxtest.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
