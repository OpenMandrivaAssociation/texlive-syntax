# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/syntax
# catalog-date 2009-10-01 19:53:35 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-syntax
Version:	20091001
Release:	5
Summary:	Creation of syntax diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/syntax
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntax.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/syntax.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091001-2
+ Revision: 756421
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091001-1
+ Revision: 719627
- texlive-syntax
- texlive-syntax
- texlive-syntax
- texlive-syntax

